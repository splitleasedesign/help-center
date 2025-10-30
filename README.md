# Split Lease Help Center - Complete Documentation

## 📋 Project Overview

This is a complete Help Center system for Split Lease, reverse-engineered from Shortstay's help center design and adapted with Split Lease branding, content, and structure.

**Brand Colors:**
- Primary: `#31135d` (Deep Purple)
- Secondary: `#FFFFFF` (White)
- Icons: Feather Icons in `#31135d`

**Project Status:** ✅ Complete Foundation Ready for Review

---

## 📁 Project Structure

```
split-lease-help-center/
│
├── index.html                 # Main hub page with 4 category cards
├── README.md                  # This documentation file
│
├── css/
│   └── style.css             # Complete design system with Split Lease branding
│
├── categories/
│   ├── guests.html           # For Guests category page (25 articles)
│   ├── hosts.html            # For Hosts category page (20 articles)
│   ├── about.html            # About Split Lease category page (3 articles)
│   └── support.html          # Support & Legal category page (2+ articles)
│
└── articles/
    ├── guests/
    │   ├── getting-started/
    │   │   └── vs-airbnb.html        # Sample: Split Lease vs Airbnb
    │   ├── before-booking/
    │   ├── trial-nights/
    │   ├── booking/
    │   ├── pricing/
    │   └── during-stay/
    │
    └── hosts/
        ├── getting-started/
        ├── listing/
        ├── legal/
        │   └── tenant-rights.html    # Sample: Tenant Rights Protections
        ├── managing/
        └── management/
```

---

## 🎨 Design System

### Color Palette

| Purpose | Color Name | Hex Code | Usage |
|---------|-----------|----------|-------|
| Primary Brand | Deep Purple | `#31135d` | Headers, buttons, icons, links |
| Background | White | `#FFFFFF` | Page backgrounds |
| Success | Light Green | `#E8F5E9` | Success messages, tips |
| Info | Light Purple | `#F3E5F5` | Info boxes, highlights |
| Text Primary | Dark Gray | `#2C2C2C` | Main content |
| Text Secondary | Medium Gray | `#666666` | Supporting text |
| Text Tertiary | Light Gray | `#999999` | Metadata, breadcrumbs |

### Typography

- **Font Stack:** System fonts (San Francisco, Segoe UI, Roboto, Arial)
- **H1:** 32px (Page titles)
- **H2:** 24px (Section headings)
- **H3:** 20px (Subsections)
- **Body:** 16px (Content)
- **Small:** 14px (Metadata)

### Icons

**Source:** [Feather Icons](https://feathericons.com)
**Implementation:** CDN via `<script src="https://unpkg.com/feather-icons"></script>`
**Color:** `#31135d`
**Initialize:** `feather.replace();` in JavaScript

**Key Icons Used:**
- `home` - Home/breadcrumb
- `search` - Search functionality
- `user` - Guest category
- `users` - Host category
- `info` - About/info
- `life-buoy` - Support
- `arrow-right` - Article links
- `chevron-right` - Breadcrumbs
- `help-circle` - Info boxes
- `check-circle` - Success boxes
- `mail` - Email contact
- `message-circle` - Chat/messaging

---

## 📊 Content Structure

### Categories & Article Count

| Category | Subcategories | Articles | Description |
|----------|--------------|----------|-------------|
| **For Guests** | 6 | 25 | Finding spaces, booking, pricing, managing rentals |
| **For Hosts** | 5 | 20 | Listing spaces, managing bookings, legal info |
| **About Split Lease** | 2 | 3 | Company info, mission, contact |
| **Support** | 1 | 2+ | Legal policies, terms, support resources |
| **TOTAL** | **14** | **48+** | |

### Guest Subcategories

1. **Getting Started** - What is Split Lease, who benefits, how to start
2. **Before You Book** - Research, verification, storage options
3. **Trial Nights** - Trial night benefits and process
4. **Booking Process** - Approval times, periodic tenancy, guarantees
5. **Pricing & Payments** - How to save money, payment methods
6. **During Your Stay** - Self-cleaning, cancellations, expectations

### Host Subcategories

1. **Getting Started** - Costs, fees, licenses, advantages
2. **Listing Your Space** - Multiple properties, storage, visibility
3. **Legal, Taxes & Agreements** - Responsibilities, tax benefits, tenant rights
4. **Managing Bookings** - Guest verification, notifications, payments
5. **Listing Management** - Updates, visibility, cancellation policies

---

## 🧩 UI Components

### 1. Header Component

Location: Top of every page
Features:
- Split Lease logo (links to hub)
- "Go to Split Lease" button

```html
<header class="header">
    <div class="container">
        <div class="header-content">
            <a href="index.html" class="logo">
                <i data-feather="home"></i>
                Split Lease Help Center
            </a>
            <nav class="header-nav">
                <a href="https://split.lease" class="btn-header" target="_blank">Go to Split Lease</a>
            </nav>
        </div>
    </div>
</header>
```

### 2. Search Banner Component

Location: Hub page and optionally on category pages
Features:
- Gradient purple background
- Centered search input
- Search icon

```html
<section class="search-banner">
    <div class="container">
        <h1>How can we help you?</h1>
        <p>Search for answers or browse our help articles below</p>
        <div class="search-container">
            <div class="search-input-wrapper">
                <i data-feather="search" class="search-icon"></i>
                <input type="text" class="search-input" placeholder="Search for help...">
            </div>
        </div>
    </div>
</section>
```

### 3. Breadcrumb Navigation

Location: Below header on all pages except hub
Features:
- Home icon + links to parent categories
- Current page indicator

```html
<div class="breadcrumb">
    <a href="../../../index.html">
        <i data-feather="home"></i>
        All Collections
    </a>
    <i data-feather="chevron-right"></i>
    <a href="../../../categories/guests.html">For Guests</a>
    <i data-feather="chevron-right"></i>
    <span class="current">Article Title</span>
</div>
```

### 4. Category Cards

Location: Hub page
Features:
- Icon, title, description
- Article count
- Hover effects

```html
<a href="categories/guests.html" class="category-card">
    <div class="category-card-icon">
        <i data-feather="user"></i>
    </div>
    <h3>For Guests</h3>
    <p>Complete guide for finding spaces and booking</p>
    <div class="category-card-meta">
        <i data-feather="file-text"></i>
        <span>25 articles</span>
    </div>
</a>
```

### 5. Info Boxes

Two variants: Info (purple) and Success (green)

**Info Box:**
```html
<div class="info-box info">
    <div class="info-box-icon">
        <i data-feather="help-circle"></i>
    </div>
    <div class="info-box-content">
        <p><strong>Title</strong></p>
        <p>Important information here</p>
    </div>
</div>
```

**Success Box:**
```html
<div class="info-box success">
    <div class="info-box-icon">
        <i data-feather="check-circle"></i>
    </div>
    <div class="info-box-content">
        <p><strong>Title</strong></p>
        <p>Success or tip message</p>
    </div>
</div>
```

### 6. Sidebar Navigation

Location: Right side of article pages
Features:
- List of related articles
- Active page highlight
- Help box

```html
<aside class="article-sidebar">
    <nav class="sidebar-nav">
        <h4>In This Section</h4>
        <ul>
            <li><a href="article1.html">Article 1</a></li>
            <li><a href="article2.html" class="active">Article 2</a></li>
            <li><a href="article3.html">Article 3</a></li>
        </ul>
    </nav>
</aside>
```

### 7. Feedback Section

Location: Bottom of article pages
Features:
- 3 emoji buttons (sad, neutral, happy)
- Click interaction

```html
<section class="feedback-section">
    <h3>Did this answer your question?</h3>
    <div class="feedback-buttons">
        <button class="feedback-btn" data-feedback="no">
            <span class="feedback-emoji">😞</span>
            <span class="feedback-label">No</span>
        </button>
        <button class="feedback-btn" data-feedback="somewhat">
            <span class="feedback-emoji">😐</span>
            <span class="feedback-label">Somewhat</span>
        </button>
        <button class="feedback-btn" data-feedback="yes">
            <span class="feedback-emoji">😄</span>
            <span class="feedback-label">Yes</span>
        </button>
    </div>
</section>
```

### 8. Footer Component

Location: Bottom of every page
Features:
- Contact information
- Policy links
- Copyright notice

```html
<footer class="footer">
    <div class="container">
        <div class="footer-content">
            <h3>Split Lease Help Center</h3>
            <p class="text-muted">Your guide to multi-local living</p>

            <div class="footer-contact">
                <div class="contact-item">
                    <i data-feather="mail"></i>
                    <a href="mailto:support@split.lease">support@split.lease</a>
                </div>
            </div>

            <div class="footer-links">
                <a href="https://split.lease/policies/terms-of-use">Terms of Use</a>
                <span>•</span>
                <a href="https://split.lease/policies">Privacy Policy</a>
            </div>
        </div>
    </div>
</footer>
```

---

## 📝 How to Create New Articles

### Step 1: Create HTML File

Place in appropriate category folder:
- Guest articles: `articles/guests/[subcategory]/article-name.html`
- Host articles: `articles/hosts/[subcategory]/article-name.html`

### Step 2: Use Article Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Brief description for SEO">
    <title>Article Title - Split Lease Help Center</title>
    <link rel="stylesheet" href="../../../css/style.css">
    <script src="https://unpkg.com/feather-icons"></script>
</head>
<body>

    <!-- Header (copy from existing article) -->

    <!-- Breadcrumb (update paths) -->

    <main class="container-narrow">
        <div class="article-layout">

            <article class="article-content">
                <div class="article-header">
                    <h1>Your Article Title</h1>
                </div>

                <div class="article-body">
                    <!-- Your content here -->
                    <p>Content...</p>

                    <!-- Use info boxes for important notes -->
                    <div class="info-box info">
                        <div class="info-box-icon">
                            <i data-feather="help-circle"></i>
                        </div>
                        <div class="info-box-content">
                            <p><strong>Note</strong></p>
                            <p>Important information</p>
                        </div>
                    </div>
                </div>

                <!-- Feedback Section (copy from existing article) -->

            </article>

            <!-- Sidebar (update links for this section) -->

        </div>
    </main>

    <!-- Footer (copy from existing article) -->

    <script>
        feather.replace();

        // Feedback functionality (copy from existing article)
    </script>

</body>
</html>
```

### Step 3: Add to Category Page

Update the appropriate category page (`categories/guests.html` or `categories/hosts.html`) to include a link to your new article:

```html
<li class="article-list-item">
    <a href="../articles/guests/subcategory/your-article.html">
        <i data-feather="arrow-right"></i>
        Your Article Title
    </a>
</li>
```

---

## 🎯 Key Features Implemented

### ✅ Completed Features

- [x] Responsive design (desktop, tablet, mobile)
- [x] Split Lease branding (#31135d, white)
- [x] Feather Icons integration
- [x] Category organization (4 main categories)
- [x] Breadcrumb navigation
- [x] Search bar UI (functionality can be added)
- [x] Info/Success boxes
- [x] Sidebar navigation
- [x] Emoji feedback system
- [x] Article list styling
- [x] Footer with contact info
- [x] Hover effects and transitions
- [x] Print-friendly styles

### 🔲 Future Enhancements (Optional)

- [ ] Actual search functionality (requires backend or JS search library)
- [ ] Analytics tracking for feedback buttons
- [ ] Language selector
- [ ] Dark mode toggle
- [ ] Article view counter
- [ ] Related articles algorithm
- [ ] Full-text search with autocomplete
- [ ] PDF export for articles

---

## 📱 Responsive Breakpoints

**Desktop:** 1200px+ (full layout with sidebar)
**Tablet:** 968px - 1199px (single column, sidebar below)
**Mobile:** 640px and below (compact layout, stacked elements)

Key responsive features:
- Sidebar moves below content on tablet/mobile
- Category cards stack on mobile
- Header navigation adapts
- Search bar maintains prominence
- Footer stacks vertically on mobile

---

## 🚀 Getting Started

### To View the Help Center:

1. Open `index.html` in a web browser
2. Navigate through categories
3. View sample articles:
   - `articles/guests/getting-started/vs-airbnb.html`
   - `articles/hosts/legal/tenant-rights.html`

### To Deploy:

1. **Simple Hosting:** Upload entire folder to web server
2. **Subdomain:** Deploy to `help.split.lease` or `support.split.lease`
3. **Integration:** Link from main Split Lease site navigation

### To Customize:

1. **Colors:** Edit CSS variables in `css/style.css` (`:root` section)
2. **Content:** Edit HTML files directly or create new articles
3. **Icons:** Browse [Feather Icons](https://feathericons.com) and replace `data-feather` values
4. **Layout:** Modify CSS grid/flexbox layouts in stylesheet

---

## 🔧 Technical Notes

### Dependencies

**External:**
- Feather Icons (CDN): `https://unpkg.com/feather-icons`

**Internal:**
- `css/style.css` - All styling
- No JavaScript frameworks required
- Pure HTML/CSS/Vanilla JS

### Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

### Performance

- Minimal external dependencies
- CSS variables for easy theming
- Optimized icons via Feather Icons
- Fast page loads (< 50KB per page)

---

## 📚 Content Mapping Reference

### From Original FAQ to Help Center

**General Questions** → Split between "For Guests > Getting Started" and "About Split Lease"
**Guest FAQ** → "For Guests" (6 subcategories)
**Host FAQ** → "For Hosts" (5 subcategories)

Total: 48 FAQ items organized into 14 subcategories across 4 main categories

---

## 🎨 Design Adaptations from Shortstay

### What We Kept:
- Overall layout structure
- Category organization approach
- Breadcrumb navigation system
- Info/success box patterns
- Sidebar navigation concept
- Emoji feedback system
- Search bar prominence

### What We Changed:
- **Color scheme:** Blue → Purple (#31135d)
- **Icons:** Generic → Feather Icons
- **Content:** Shortstay → Split Lease
- **Categories:** 7 → 4 (more focused)
- **Terminology:** Multi-local focused
- **Emphasis:** Trial nights, split schedules, periodic tenancy

### What We Added:
- Tax benefit messaging
- Periodic tenancy education
- Trial night prominence
- Guest-guest-landlord relationships
- Protection mechanisms for hosts

---

## 📞 Support & Contact

**Project Creator:** Claude Code
**Date Created:** October 27, 2025
**Version:** 1.0

**For Split Lease:**
- Email: support@split.lease
- Website: https://split.lease
- Help Center: (this project)

---

## 📋 Next Steps

### Immediate Next Steps:
1. ✅ Review structure and design
2. ⏳ Create remaining article pages (46 articles total)
3. ⏳ Implement actual search functionality (optional)
4. ⏳ Deploy to staging environment
5. ⏳ User testing and feedback
6. ⏳ Production deployment

### Content Creation Priority:
**High Priority Articles:**
- What is Split Lease
- How to get started
- Trial night explanations
- Pricing and savings
- Tax benefits for hosts
- Tenant rights protections

**Medium Priority:**
- All booking process articles
- All listing management articles
- Payment and fee explanations

**Low Priority:**
- Edge cases and troubleshooting
- Advanced features
- Policy details (link to main site)

---

## 🏆 Project Completion Summary

### What's Been Delivered:

1. **Complete Design System** - CSS with Split Lease branding
2. **Hub Page** - Main entry point with 4 categories
3. **4 Category Pages** - Guests, Hosts, About, Support
4. **2 Sample Articles** - Fully formatted with all components
5. **Comprehensive Documentation** - This README
6. **Scalable Structure** - Easy to add new articles

### Estimated Time to Complete All Articles:

- Average: 15-20 minutes per article
- Total: 46 articles remaining
- Estimated: 12-15 hours of content writing

### File Count:

- **Created:** 11 files
- **Ready to Create:** 46 article files
- **Total Project:** ~57 files when complete

---

**🎉 Project ready for review and expansion!**

---

## 🗺️ Quick Reference: File Paths

### Hub & Categories
```
index.html
categories/guests.html
categories/hosts.html
categories/about.html
categories/support.html
```

### Sample Articles
```
articles/guests/getting-started/vs-airbnb.html
articles/hosts/legal/tenant-rights.html
```

### Assets
```
css/style.css
```

---

**End of Documentation**
