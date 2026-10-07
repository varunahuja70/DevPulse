#!/usr/bin/env python3
"""
DevPulse Setup & Automation Script
Version: 1.22.2
Author: Varun Ahuja (https://github.com/varunahuja70/DevPulse)

Usage:
    python setup.py build       # Builds hook, compiles release NSIS bundle, updates DevPulse-Setup.exe
    python setup.py test        # Runs JavaScript & Rust test suites
    python setup.py dev         # Launches DevPulse in local development mode
    python setup.py run         # Launches the compiled DevPulse binary
    python setup.py check       # Checks prerequisites (Rust, Node, WebView2)
"""

import sys
import os
import shutil
import subprocess
import argparse
from pathlib import Path

# Ensure UTF-8 output handling on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

VERSION = "1.22.2"
APP_NAME = "DevPulse"
ROOT_DIR = Path(__file__).resolve().parent

def log(msg, symbol="[*]"):
    print(f"\n{symbol} {msg}")

def run_cmd(cmd, cwd=None, check=True):
    print(f"  -> Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    res = subprocess.run(cmd, cwd=cwd or ROOT_DIR, shell=True)
    if check and res.returncode != 0:
        print(f"[!] Command failed with return code {res.returncode}")
        sys.exit(res.returncode)
    return res

def check_env():
    log(f"Checking environment prerequisites for {APP_NAME} v{VERSION}...")
    tools = {
        "cargo": "Rust & Cargo (https://rustup.rs/)",
        "node": "Node.js (https://nodejs.org/)",
        "npm": "NPM package manager",
    }
    missing = []
    for tool, desc in tools.items():
        if shutil.which(tool) is None:
            missing.append(f"- {tool}: {desc}")
        else:
            print(f"  [+] Found {tool}")

    if missing:
        print("\n[!] Missing required build tools:")
        print("\n".join(missing))
        sys.exit(1)
    print("  [+] All prerequisites detected.")

def run_tests():
    log("Running DevPulse test suite...")
    test_files = [
        "test-carry.cjs",
        "test-codex-headline.cjs",
        "test-light-surface.cjs",
        "test-reset-card.cjs"
    ]
    cmd = ["node", "--test"] + test_files
    run_cmd(cmd)
    print("[+] All test suites passed!")

def build_app():
    check_env()
    log(f"Building {APP_NAME} v{VERSION} release installer...")

    # Step 1: Build the hook library
    log("Building codenotch-hook library...", symbol="[1/3]")
    run_cmd("cargo build --release -p codenotch-hook --target-dir target/hook")

    # Step 2: Build Tauri application & NSIS installer
    log("Bundling Windows NSIS Installer with Tauri CLI...", symbol="[2/3]")
    run_cmd("npx @tauri-apps/cli build")

    # Step 3: Copy to root DevPulse-Setup.exe
    target_bundle = ROOT_DIR / "target" / "release" / "bundle" / "nsis" / f"DevPulse_{VERSION}_x64-setup.exe"
    dest_exe = ROOT_DIR / "DevPulse-Setup.exe"

    if target_bundle.exists():
        shutil.copy2(target_bundle, dest_exe)
        log(f"Installer successfully created:\n   -> {target_bundle}\n   -> {dest_exe}", symbol="[3/3]")
    else:
        # Check if any setup exe exists
        found = list((ROOT_DIR / "target" / "release" / "bundle" / "nsis").glob("*setup.exe"))
        if found:
            shutil.copy2(found[0], dest_exe)
            log(f"Installer copied from {found[0]} to {dest_exe}", symbol="[3/3]")
        else:
            print("[!] Setup executable was not found in target bundle folder.")
            sys.exit(1)

def run_dev():
    check_env()
    log("Launching DevPulse in development mode...", symbol="[>]")
    run_cmd("npx @tauri-apps/cli dev", cwd=ROOT_DIR / "codenotch")

def run_installed():
    target_exe = ROOT_DIR / "target" / "release" / "codenotch.exe"
    if not target_exe.exists():
        print(f"[!] Binary not found at {target_exe}. Please run 'python setup.py build' first.")
        sys.exit(1)
    log(f"Launching {APP_NAME}...", symbol="[>]")
    subprocess.Popen([str(target_exe)])

def main():
    parser = argparse.ArgumentParser(
        description=f"{APP_NAME} Setup & Build Automation (v{VERSION})",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python setup.py build       # Compile and bundle DevPulse installer
  python setup.py test        # Run unit tests
  python setup.py dev         # Run local dev server
  python setup.py check       # Verify Rust, Node.js, and dependencies
  python setup.py run         # Launch built application
        """
    )
    parser.add_argument(
        "action",
        nargs="?",
        default="build",
        choices=["build", "test", "dev", "run", "check"],
        help="Action to execute (default: build)"
    )

    args = parser.parse_args()

    if args.action == "check":
        check_env()
    elif args.action == "test":
        run_tests()
    elif args.action == "build":
        run_tests()
        build_app()
    elif args.action == "dev":
        run_dev()
    elif args.action == "run":
        run_installed()

if __name__ == "__main__":
    main()
