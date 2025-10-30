#!/usr/bin/env python3
"""
Fix headers in Split Lease Help Center articles
Replace purple header (main-header) with white header (header) in all article pages
Keep purple header only on main index.html
"""

import re
import os
from pathlib import Path

def get_white_header(depth):
    """Generate the white header with correct relative paths based on depth"""
    prefix = "../" * depth

    return f'''    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <a href="{prefix}index.html" class="logo">
                    <img src="https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2F50bf0464e4735aabad1cc8848a0e8b8a.cdn.bubble.io%2Ff1587601671931x294112149689599100%2Fsplit%2520lease%2520purple%2520circle.png?w=48&h=&auto=enhance&dpr=1&q=100&fit=max" alt="Split Lease" style="width: 32px; height: 32px; margin-right: 8px;">
                    Split Lease Help Center
                </a>
                <nav class="header-nav">
                    <a href="https://split.lease" class="btn-header" target="_blank">Go to Split Lease</a>
                </nav>
            </div>
        </div>
    </header>'''

def calculate_depth(file_path):
    """Calculate the depth of a file relative to the root"""
    parts = Path(file_path).parts
    # Count how many directories deep we are
    return len(parts) - 1  # -1 because we don't count the filename

def fix_header_in_file(file_path):
    """Replace old header with new header (with logo) in a single file"""
    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if this file has a header to replace (purple or white)
        if 'class="main-header"' not in content and 'class="header"' not in content:
            print(f"  [-] Skipping (no header found)")
            return 'skipped'

        # Calculate depth for relative paths
        depth = calculate_depth(file_path)
        white_header = get_white_header(depth)

        # Pattern to match any header (purple or white)
        # Try different patterns
        patterns = [
            r'    <!-- Split Lease Header Navigation -->.*?</header>',  # Purple with comment
            r'    <header class="main-header">.*?</header>',  # Purple without comment
            r'    <!-- Header -->.*?</header>',  # White header with comment
            r'    <header class="header">.*?</header>',  # White header without comment
        ]

        pattern_found = None
        for pattern in patterns:
            if re.search(pattern, content, re.DOTALL):
                pattern_found = pattern
                break

        if not pattern_found:
            print(f"  [WARNING] Could not find header pattern")
            return 'error'

        # Replace old header with new header (with logo)
        new_content = re.sub(pattern_found, white_header, content, flags=re.DOTALL)

        # Also need to remove the split-lease-header-footer.css link if present
        new_content = re.sub(
            r'    <link rel="stylesheet" href="[^"]*split-lease-header-footer\.css">\n',
            '',
            new_content
        )

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  [OK] Fixed successfully")
        return 'fixed'

    except Exception as e:
        print(f"  [ERROR] {e}")
        return 'error'

def main():
    """Main function to fix all article headers"""
    print("="*70)
    print("Split Lease Help Center - Update Headers with Logo")
    print("="*70)
    print("\nUpdating all article headers to use company logo...")
    print("(Keeping purple header only on main index.html)\n")

    # Find all HTML files with headers, excluding the main index.html
    files_to_process = []

    # Walk through the directory
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # Normalize path
                file_path = os.path.normpath(file_path)

                # Skip the main index.html (keep purple header there)
                if file_path == 'index.html' or file_path == '.\\index.html':
                    print(f"Skipping main index.html (keeping purple header)")
                    continue

                # Skip category pages (they should also get the logo)
                # Actually, let's include category pages too
                # if 'categories' in file_path:
                #     continue

                # Check if file has any header (purple or white)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'class="main-header"' in content or 'class="header"' in content:
                            files_to_process.append(file_path)
                except:
                    pass

    print(f"\nFound {len(files_to_process)} files to process\n")
    print("-"*70)

    stats = {'fixed': 0, 'skipped': 0, 'error': 0}

    for file_path in files_to_process:
        result = fix_header_in_file(file_path)
        stats[result] += 1

    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"[OK] Fixed:   {stats['fixed']} files")
    print(f"[-] Skipped:  {stats['skipped']} files")
    print(f"[X] Errors:   {stats['error']} files")
    print("="*70)

    if stats['error'] == 0:
        print("\n[SUCCESS] All headers updated successfully!")
    else:
        print(f"\n[WARNING] {stats['error']} file(s) had errors. Please review.")

if __name__ == "__main__":
    main()
