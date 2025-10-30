#!/usr/bin/env python3
"""
Fix headers in Split Lease Help Center articles
"""

import re
import os

# List of files that need header fixes (host articles without responsive header)
FILES_TO_FIX = [
    "articles/hosts/legal/legal-responsibilities.html",
    "articles/hosts/legal/tax-benefits.html",
    "articles/hosts/legal/lease-agreements.html",
    "articles/hosts/managing/see-renters.html",
    "articles/hosts/managing/notifications.html",
    "articles/hosts/managing/verify-traveler.html",
    "articles/hosts/managing/payments.html",
    "articles/hosts/management/update-listing.html",
    "articles/hosts/management/listing-visibility.html",
    "articles/hosts/management/cancellation-policy.html",
]

# The correct responsive header
RESPONSIVE_HEADER = '''    <!-- Split Lease Header Navigation -->
    <header class="main-header">
        <nav class="nav-container">
            <div class="nav-left">
                <a href="https://splitlease.app" class="logo">
                    <img src="../../../assets/images/logo.png" alt="Split Lease" class="logo-image">
                    <span class="logo-text">Split Lease</span>
                </a>
            </div>
            <button class="hamburger-menu" aria-label="Toggle navigation menu" onclick="toggleMobileMenu()">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>
            <div class="nav-center">
                <div class="nav-dropdown">
                    <a href="#host" class="nav-link dropdown-trigger" role="button" aria-expanded="false" aria-haspopup="true">
                        <span class="mobile-text">Host</span><span class="desktop-text">Host with Us</span>
                        <svg class="dropdown-arrow" width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true">
                            <path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </a>
                    <div class="dropdown-menu" role="menu" aria-label="Host with Us menu">
                        <a href="https://app.split.lease/host-step-by-step-guide-to-list" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">Why List with Us</span>
                            <span class="dropdown-desc">New to Split Lease? Learn more about hosting</span>
                        </a>
                        <a href="https://app.split.lease/success-stories-guest" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">Success Stories</span>
                            <span class="dropdown-desc">Explore other hosts' feedback</span>
                        </a>
                        <a href="https://app.split.lease/signup-login" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">List Property</span>
                        </a>
                        <a href="https://app.split.lease/policies/cancellation-and-refund-policy" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">Legal Information</span>
                            <span class="dropdown-desc">Review most important policies</span>
                        </a>
                        <a href="../../../categories/hosts.html" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">FAQs</span>
                            <span class="dropdown-desc">Frequently Asked Questions</span>
                        </a>
                        <a href="https://app.split.lease/signup-login" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">Sign Up</span>
                        </a>
                    </div>
                </div>
                <div class="nav-dropdown">
                    <a href="#stay" class="nav-link dropdown-trigger" role="button" aria-expanded="false" aria-haspopup="true">
                        <span class="mobile-text">Guest</span><span class="desktop-text">Stay with Us</span>
                        <svg class="dropdown-arrow" width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true">
                            <path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </a>
                    <div class="dropdown-menu" role="menu" aria-label="Stay with Us menu">
                        <a href="https://app.split.lease/search" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">Explore Rentals</span>
                            <span class="dropdown-desc">See available listings!</span>
                        </a>
                        <a href="https://app.split.lease/success-stories-guest" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">Success Stories</span>
                            <span class="dropdown-desc">Explore other guests' feedback</span>
                        </a>
                        <a href="../../../categories/guests.html" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">FAQs</span>
                            <span class="dropdown-desc">Frequently Asked Questions</span>
                        </a>
                        <a href="https://app.split.lease/signup-login" class="dropdown-item" role="menuitem">
                            <span class="dropdown-title">Sign Up</span>
                        </a>
                    </div>
                </div>
            </div>
            <div class="nav-right">
                <a href="https://app.split.lease/search" class="explore-rentals-btn">Explore Rentals</a>
                <a href="https://app.split.lease/signup-login" class="nav-link">Sign In</a>
                <span class="divider">|</span>
                <a href="https://app.split.lease/signup-login" class="nav-link">Sign Up</a>
            </div>
        </nav>
    </header>'''

def fix_header(file_path):
    """Replace the simplified header with the responsive header"""
    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern to match the simplified header (all on one line or multiline)
        pattern = r'<header class="main-header">.*?</header>'

        # Replace with responsive header
        new_content = re.sub(pattern, RESPONSIVE_HEADER.strip(), content, flags=re.DOTALL)

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[OK] Fixed: {file_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Error fixing {file_path}: {e}")
        return False

def main():
    """Main function to fix all headers"""
    print("Starting header fix process...")
    print(f"Will fix {len(FILES_TO_FIX)} files\n")

    fixed_count = 0
    error_count = 0

    for file_path in FILES_TO_FIX:
        if os.path.exists(file_path):
            if fix_header(file_path):
                fixed_count += 1
            else:
                error_count += 1
        else:
            print(f"[ERROR] File not found: {file_path}")
            error_count += 1

    print(f"\n{'='*50}")
    print(f"Header fix complete!")
    print(f"Fixed: {fixed_count} files")
    print(f"Errors: {error_count} files")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
