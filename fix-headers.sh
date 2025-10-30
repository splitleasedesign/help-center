#!/bin/bash

# Script to fix headers in all article files

FILES=(
  "articles/guests/booking/approval-time.html"
  "articles/guests/booking/booking-timeline.html"
  "articles/guests/booking/periodic-tenancy.html"
  "articles/guests/booking/money-back-guarantee.html"
  "articles/guests/pricing/save-money.html"
  "articles/guests/pricing/credit-card-approval.html"
  "articles/guests/during-stay/self-cleaning.html"
  "articles/guests/during-stay/cancel-stay.html"
  "articles/guests/during-stay/not-meeting-expectations.html"
  "articles/hosts/getting-started/listing-costs.html"
  "articles/hosts/getting-started/host-fees.html"
  "articles/hosts/getting-started/rental-license.html"
  "articles/hosts/getting-started/advantages.html"
  "articles/hosts/listing/multiple-properties.html"
  "articles/hosts/listing/live-in-listing.html"
  "articles/hosts/listing/public-information.html"
  "articles/hosts/listing/storage-area.html"
  "articles/hosts/listing/damage-deposit.html"
  "articles/hosts/legal/legal-responsibilities.html"
  "articles/hosts/legal/tax-benefits.html"
  "articles/hosts/legal/lease-agreements.html"
  "articles/hosts/managing/see-renters.html"
  "articles/hosts/managing/notifications.html"
  "articles/hosts/managing/verify-traveler.html"
  "articles/hosts/managing/payments.html"
  "articles/hosts/management/update-listing.html"
  "articles/hosts/management/listing-visibility.html"
  "articles/hosts/management/cancellation-policy.html"
)

GOOD_HEADER='    <!-- Split Lease Header Navigation -->
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
                            <span class="dropdown-desc">Explore other hosts\47 feedback</span>
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
                            <span class="dropdown-desc">Explore other guests\47 feedback</span>
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
    </header>'

echo "Starting header fix process..."
echo "This will update ${#FILES[@]} files"

for FILE in "${FILES[@]}"; do
  if [ -f "$FILE" ]; then
    echo "Processing: $FILE"

    # Create a Python script to do the replacement
    python3 << 'PYTHON_SCRIPT'
import re
import sys

file_path = sys.argv[1]

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the replacement header
good_header = '''    <!-- Split Lease Header Navigation -->
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

# Replace the header - match from <header to </header>
pattern = r'<header class="main-header">.*?</header>'
new_content = re.sub(pattern, good_header.strip(), content, flags=re.DOTALL)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {file_path}")
PYTHON_SCRIPT "$FILE"
  else
    echo "File not found: $FILE"
  fi
done

echo "Header fix complete!"
