#!/usr/bin/env python3
"""
Remove home icons from breadcrumb navigation in Split Lease Help Center
"""

import re
import os
from pathlib import Path

def remove_breadcrumb_icon(file_path):
    """Remove the home icon from breadcrumb navigation in a single file"""
    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if this file has a breadcrumb with home icon
        if '<i data-feather="home"></i>' not in content or 'breadcrumb' not in content:
            print(f"  [-] Skipping (no breadcrumb with home icon)")
            return 'skipped'

        # Pattern to match the home icon in breadcrumbs
        # Match: <a href="...index.html">\n            <i data-feather="home"></i>\n            All Collections\n        </a>
        # Replace with: <a href="...index.html">All Collections</a>

        pattern = r'(<a href="[^"]*index\.html")\s*>\s*<i data-feather="home"></i>\s*(All Collections)\s*</a>'
        replacement = r'\1>\2</a>'

        # Replace the pattern
        new_content = re.sub(pattern, replacement, content)

        # Check if anything was changed
        if new_content == content:
            print(f"  [-] No changes needed")
            return 'skipped'

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  [OK] Removed home icon from breadcrumb")
        return 'fixed'

    except Exception as e:
        print(f"  [ERROR] {e}")
        return 'error'

def main():
    """Main function to remove home icons from all breadcrumbs"""
    print("="*70)
    print("Split Lease Help Center - Remove Breadcrumb Home Icons")
    print("="*70)
    print("\nRemoving home icons from breadcrumb navigation...\n")

    # Find all HTML files
    files_to_process = []

    # Walk through the directory
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # Normalize path
                file_path = os.path.normpath(file_path)

                # Skip the main index.html (no breadcrumb there)
                if file_path == 'index.html' or file_path == '.\\index.html':
                    continue

                # Check if file has breadcrumb
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'breadcrumb' in content:
                            files_to_process.append(file_path)
                except:
                    pass

    print(f"Found {len(files_to_process)} files with breadcrumbs\n")
    print("-"*70)

    stats = {'fixed': 0, 'skipped': 0, 'error': 0}

    for file_path in files_to_process:
        result = remove_breadcrumb_icon(file_path)
        stats[result] += 1

    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"[OK] Fixed:   {stats['fixed']} files")
    print(f"[-] Skipped:  {stats['skipped']} files")
    print(f"[X] Errors:   {stats['error']} files")
    print("="*70)

    if stats['error'] == 0:
        print("\n[SUCCESS] All breadcrumb icons removed successfully!")
    else:
        print(f"\n[WARNING] {stats['error']} file(s) had errors. Please review.")

if __name__ == "__main__":
    main()
