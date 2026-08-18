#!/usr/bin/env python3
"""Generate the static pages for the Shreeja Marine site.

The header, mobile nav and footer live here once so every page is
guaranteed to ship the same markup. Run from the repo root:

    python src/build_pages.py
"""
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

BRAND = "Shreeja Marine Services"
EMAIL = "info@shreeja.co.in"
PHONE = "+91-8318249677"
PHONE_HREF = "+918318249677"
ADDRESS = ("311, 3rd Floor, NBC Complex, Sector-11, Plot No. 43, "
           "CBD Belapur, Maharashtra - 400617")
FORM_ACTION = "https://formsubmit.co/Info@shreeja.co.in"

SERVICES = [
    ("technical-management", "Technical Management",
     "End-to-end technical management support to ensure vessels remain seaworthy, safe, and operationally optimized.",
     "services-slider-technical-management-1024x491.png"),
    ("crew-management", "Crew Management",
     "Managing the full lifecycle of seafaring personnel with tailored manning solutions for all types of vessels.",
     "crew-management-banner-1024x491.webp"),
    ("marine-insurance", "Marine Insurance",
     "Tailored marine insurance products protecting stakeholders against maritime risks and providing financial security.",
     "financial-administration-banner-1024x491.webp"),
    ("e-migrate-service", "E-Migrate Service",
     "Assistance in navigating the mandatory DG Shipping E-Migrate system for Indian seafarers and recruiting agencies.",
     "services-slider-training-1024x491.png"),
    ("flag-documentation", "Flag Documentation",
     "Acting as a liaison between vessel owners and flag administrations to facilitate registration and compliance.",
     "chartering-broking-banner-1024x491.webp"),
]

SERVICE_DETAIL = {
    "technical-management": (
        "Shreeja Marine Services provides end-to-end technical management support to "
        "ensure vessels remain seaworthy, safe, and operationally optimized.",
        [("Planned Maintenance Systems (PMS)", "Monitoring and upkeep of fleet condition"),
         ("Dry Docking &amp; Repairs", "Management of vessel repairs and maintenance projects"),
         ("Technical Supervision", "Oversight by experienced marine engineers and surveyors"),
         ("Procurement &amp; Budgeting", "Handling spare parts, machinery procurement, and operational budget management"),
         ("Compliance", "Ensuring adherence to class and flag state technical requirements")]),
    "crew-management": (
        "Shreeja Marine Services manages the full lifecycle of seafaring personnel, providing "
        "tailored manning solutions for bulk carriers, tankers, container ships, and offshore vessels.",
        [("Recruitment &amp; Placement", "Sourcing and vetting qualified officers, engineers, and ratings"),
         ("Certification &amp; Documentation", "Handling STCW/MLC compliance, flag endorsements, and medical certificates"),
         ("Payroll &amp; HR", "Managing payroll, allotments, and performance monitoring"),
         ("Logistics &amp; Training", "Arranging travel, visas, and comprehensive training programs")]),
    "marine-insurance": (
        "Shreeja Marine Services offers tailored marine insurance products to protect stakeholders "
        "against maritime risks, providing financial security against potential losses.",
        [("Hull &amp; Machinery Insurance", "Protection for vessel structure and equipment"),
         ("Cargo Insurance", "Coverage for goods in transit"),
         ("Protection &amp; Indemnity (P&amp;I)", "Third-party liability coverage"),
         ("Marine Liability Insurance", "Coverage for environmental damage and legal disputes"),
         ("War &amp; Piracy Risk Cover", "Protection against conflict-related risks")]),
    "e-migrate-service": (
        "Shreeja Marine Services assists seafarers and recruiting agencies in navigating the DG "
        "Shipping E-Migrate system, which is mandatory for Indian seafarers engaged on foreign or "
        "Indian-flagged vessels.",
        [("Registration Compliance", "Ensuring seafarers and recruiting agencies follow government-mandated registration and data-filing procedures"),
         ("Documentation Support", "Generating required forms (e.g., Form-I) for immigration clearance, including vessel/seafarer details and sign-on/sign-off dates"),
         ("Process Guidance", "End-to-end assistance with the e-Migrate portal and regulatory requirements")]),
    "flag-documentation": (
        "Shreeja Marine Services acts as a liaison between vessel owners and flag administrations "
        "to facilitate vessel registration and ongoing compliance.",
        [("Vessel Registration", "Assistance with major open registries and flag states"),
         ("Certification", "Renewal and endorsement of Safe Manning, Tonnage, and Class Certificates"),
         ("Technical File Preparation", "Creating statutory manuals, checklists, and plans required by the flag state"),
         ("Recording", "Ownership and mortgage recording in compliance with flag state laws")]),
}

CAPABILITIES = [
    ("Full Management", "services-slider.png"),
    ("Technical Management", "services-slider-technical-management-1024x491.png"),
    ("Crew Management", "crew-management-banner-1024x491.webp"),
    ("Financial Administration", "financial-administration-banner-1024x491.webp"),
    ("Operations Management", "operations-management-banner-1024x491.webp"),
    ("Purchasing Management", "purchasing-management-banner-1024x491.webp"),
    ("Riding Squad", "services-riding-squad-1024x491.webp"),
    ("Chartering Broking", "chartering-broking-banner-1024x491.webp"),
    ("Crew Training", "services-slider-training-1024x491.png"),
]

ICON_GLOBE = ('<path d="M12 21a9 9 0 100-18 9 9 0 000 18zM3.6 9h16.8M3.6 15h16.8M12 3a15 15 0 010 18 '
              '15 15 0 010-18z"/>')
ICON_CLOCK = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
ICON_DOC = ('<path d="M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8l-5-5z"/>'
            '<path d="M14 3v5h5M9 13h6M9 17h6"/>')
ICON_SHIELD = '<path d="M12 3l7 3v6c0 4.5-3 8-7 9-4-1-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>'

HIGHLIGHTS = [
    ("Maritime Operations worldwide.", ICON_GLOBE),
    ("10+ Years Work Experiences", ICON_CLOCK),
    ("Flag Documentation Services", ICON_DOC),
    ("Marine Insurance Solutions", ICON_SHIELD),
]

STATS = [("1000", "+", "Seafarers Worldwide"), ("20", "+", "Vessels Managed"),
         ("20", "+", "Happy Clients"), ("100", "%", "Retention Rate")]


def home(p):
    """Link to the site root without exposing "index.html" in the URL.

    Returns "./" at the root and "../" / "../../" from nested pages, so the
    site still works if it is ever served from a subdirectory.
    """
    return p or "./"


def icon(path, cls="h-6 w-6"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{path}</svg>')


def head(title, desc, p):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-pt-24">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{p}assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{p}assets/css/app.css">
</head>
<body>
<a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:z-[100] focus:m-3 focus:rounded-lg focus:bg-accent focus:px-4 focus:py-2 focus:font-semibold focus:text-brand">Skip to content</a>
"""


def nav_links(p, active):
    items = [("Home", home(p), "home"),
             ("About Us", f"{p}about-us/", "about"),
             ("Services", f"{p}services/", "services"),
             ("Contact Us", f"{p}contact-us/", "contact")]
    out = []
    for label, href, key in items:
        state = "text-accent" if key == active else "text-white hover:text-accent"
        if key == "services":
            sub = "".join(
                f'<a href="{p}services/{s}/" class="block rounded-lg px-4 py-2.5 text-sm '
                f'text-headline/80 hover:bg-mist hover:text-brand">{n}</a>'
                for s, n, _, _ in SERVICES)
            out.append(f"""<div class="group relative">
  <a href="{href}" class="flex items-center gap-1.5 py-2 text-sm font-semibold transition-colors {state}">
    Services
    <svg class="h-3.5 w-3.5 transition-transform group-hover:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
  </a>
  <div class="invisible absolute left-0 top-full z-50 w-64 translate-y-1 rounded-xl border border-black/5 bg-white p-2 opacity-0 shadow-xl transition-all duration-200 group-hover:visible group-hover:translate-y-0 group-hover:opacity-100">
    <a href="{href}" class="block rounded-lg px-4 py-2.5 text-sm font-semibold text-brand hover:bg-mist">All Services</a>
    <div class="my-1 h-px bg-black/5"></div>
    {sub}
  </div>
</div>""")
        else:
            out.append(f'<a href="{href}" class="py-2 text-sm font-semibold transition-colors {state}">{label}</a>')
    return "\n".join(out)


def mobile_links(p, active):
    subs = "".join(
        f'<a href="{p}services/{s}/" class="block border-b border-white/10 py-3 pl-4 text-[15px] text-white/75 hover:text-accent">{n}</a>'
        for s, n, _, _ in SERVICES)
    return f"""<a href="{home(p)}" class="block border-b border-white/10 py-4 text-lg font-semibold {'text-accent' if active=='home' else 'text-white hover:text-accent'}">Home</a>
<a href="{p}about-us/" class="block border-b border-white/10 py-4 text-lg font-semibold {'text-accent' if active=='about' else 'text-white hover:text-accent'}">About Us</a>
<div class="border-b border-white/10">
  <button type="button" data-submenu-toggle aria-expanded="false" class="flex w-full items-center justify-between py-4 text-left text-lg font-semibold {'text-accent' if active=='services' else 'text-white hover:text-accent'}">
    <span>Services</span>
    <svg data-chevron class="h-4 w-4 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
  </button>
  <div class="hidden pb-2">
    <a href="{p}services/" class="block border-b border-white/10 py-3 pl-4 text-[15px] font-semibold text-white/90 hover:text-accent">All Services</a>
    {subs}
  </div>
</div>
<a href="{p}contact-us/" class="block border-b border-white/10 py-4 text-lg font-semibold {'text-accent' if active=='contact' else 'text-white hover:text-accent'}">Contact Us</a>"""


def header(p, active):
    return f"""<header data-header class="fixed inset-x-0 top-0 z-50 transition-all duration-300">
<div class="container-x flex h-20 items-center justify-between gap-4">
  <a href="{home(p)}" class="shrink-0" aria-label="{BRAND} home">
    <img src="{p}assets/img/logo.png" alt="{BRAND}" class="h-12 w-auto" width="150" height="48">
  </a>
  <nav class="hidden items-center gap-8 lg:flex" aria-label="Main">
    {nav_links(p, active)}
  </nav>
  <a href="{p}contact-us/" class="btn-accent hidden lg:inline-flex">Get a Quote</a>
  <button type="button" data-menu-toggle aria-expanded="false" aria-controls="mobile-menu"
          class="flex h-11 w-11 shrink-0 items-center justify-center rounded-lg text-white lg:hidden"
          aria-label="Toggle navigation menu">
    <span class="flex flex-col items-center justify-center gap-[5px]">
      <span class="block h-0.5 w-6 rounded bg-white"></span>
      <span class="block h-0.5 w-6 rounded bg-white"></span>
      <span class="block h-0.5 w-6 rounded bg-white"></span>
    </span>
  </button>
</div>
</header>

<div data-menu-backdrop class="pointer-events-none fixed inset-0 z-50 bg-black/60 opacity-0 transition-opacity duration-300 lg:hidden"></div>
<div id="mobile-menu" data-menu-panel
     class="fixed right-0 top-0 z-50 h-full w-[85%] max-w-sm translate-x-full overflow-y-auto bg-brand transition-transform duration-300 ease-out lg:hidden">
  <div class="flex h-20 items-center justify-between px-5">
    <img src="{p}assets/img/logo.png" alt="{BRAND}" class="h-10 w-auto">
    <button type="button" data-menu-toggle
            class="flex h-11 w-11 items-center justify-center rounded-lg text-white"
            aria-label="Close navigation menu">
      <svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <nav class="px-5 pb-10" aria-label="Mobile">
    {mobile_links(p, active)}
    <a href="{p}contact-us/" class="btn-accent mt-6 w-full">Get a Quote</a>
  </nav>
</div>
"""


def footer(p):
    svc = "".join(f'<li><a href="{p}services/{s}/" class="transition-colors hover:text-accent">{n}</a></li>'
                  for s, n, _, _ in SERVICES)
    return f"""<footer class="bg-brand-dark text-white/70">
<div class="container-x grid gap-10 py-16 sm:grid-cols-2 lg:grid-cols-4">
  <div>
    <img src="{p}assets/img/logo.png" alt="{BRAND}" class="h-14 w-auto" width="170" height="56">
    <p class="mt-5 text-sm leading-relaxed">Shreeja Marine is a leading company based in Mumbai providing comprehensive shipping solutions for companies across the globe.</p>
  </div>
  <div>
    <h2 class="text-base font-bold text-white">Company</h2>
    <ul class="mt-5 space-y-3 text-sm">
      <li><a href="{home(p)}" class="transition-colors hover:text-accent">Home</a></li>
      <li><a href="{p}about-us/" class="transition-colors hover:text-accent">About Us</a></li>
      <li><a href="{p}services/" class="transition-colors hover:text-accent">Services</a></li>
      <li><a href="{p}contact-us/" class="transition-colors hover:text-accent">Contact Us</a></li>
    </ul>
  </div>
  <div>
    <h2 class="text-base font-bold text-white">Services</h2>
    <ul class="mt-5 space-y-3 text-sm">{svc}</ul>
  </div>
  <div>
    <h2 class="text-base font-bold text-white">Address</h2>
    <ul class="mt-5 space-y-4 text-sm">
      <li class="flex gap-3">{icon('<path d="M12 21s7-5.5 7-11a7 7 0 10-14 0c0 5.5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>', 'h-5 w-5 shrink-0 text-accent')}<span>{ADDRESS}</span></li>
      <li class="flex gap-3">{icon('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', 'h-5 w-5 shrink-0 text-accent')}<a href="mailto:{EMAIL}" class="transition-colors hover:text-accent">{EMAIL}</a></li>
      <li class="flex gap-3">{icon('<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .3 1.9.6 2.8a2 2 0 01-.4 2.1L8.1 9.9a16 16 0 006 6l1.3-1.2a2 2 0 012.1-.4c.9.3 1.8.5 2.8.6a2 2 0 011.7 2z"/>', 'h-5 w-5 shrink-0 text-accent')}<a href="tel:{PHONE_HREF}" class="transition-colors hover:text-accent">{PHONE}</a></li>
    </ul>
  </div>
</div>
<div class="border-t border-white/10">
  <p class="container-x py-6 text-center text-sm">&copy; <span data-year>2025</span> {BRAND}. All Rights Reserved.</p>
</div>
</footer>

<a href="https://wa.me/{PHONE_HREF[1:]}" target="_blank" rel="noopener"
   class="fixed bottom-5 right-5 z-40 flex h-14 w-14 items-center justify-center rounded-full bg-[#25D366] text-white shadow-lg transition-transform hover:scale-105"
   aria-label="Chat on WhatsApp">
  <svg class="h-7 w-7" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.7 1-.9 1.2-.2.2-.3.2-.6.1a8 8 0 01-2.4-1.5 9 9 0 01-1.7-2.1c-.2-.3 0-.5.1-.6l.5-.6.3-.5v-.6l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7s1.2 3.1 1.3 3.3c.2.2 2.3 3.5 5.6 4.9 2.7 1.1 3.3.9 3.9.8.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.2-.6-.4z"/><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1112 20.2z"/></svg>
</a>

<script src="{p}assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(title, crumb, p):
    return f"""<section class="relative isolate overflow-hidden bg-brand pt-32 pb-16 sm:pt-40 sm:pb-20">
  <img src="{p}assets/img/hero-bg.jpg" alt="" class="absolute inset-0 -z-10 h-full w-full object-cover opacity-20">
  <div class="container-x">
    <h1 class="text-3xl font-extrabold text-white sm:text-4xl lg:text-5xl">{title}</h1>
    <nav class="mt-4 flex flex-wrap items-center gap-2 text-sm text-white/70" aria-label="Breadcrumb">{crumb}</nav>
  </div>
</section>"""


def highlights_block():
    cards = "".join(f"""<div class="rounded-2xl border border-black/5 bg-white p-7 shadow-sm transition-shadow hover:shadow-lg">
      <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-brand text-accent">{icon(ic, 'h-6 w-6')}</div>
      <h3 class="mt-5 text-lg leading-snug">{t}</h3>
    </div>""" for t, ic in HIGHLIGHTS)
    return f'<div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">{cards}</div>'


def stats_block():
    cells = "".join(f"""<div class="text-center">
      <p class="text-4xl font-extrabold text-accent sm:text-5xl"><span data-count-to="{n}">0</span>{sfx}</p>
      <p class="mt-2 text-sm font-semibold uppercase tracking-wider text-white/70">{label}</p>
    </div>""" for n, sfx, label in STATS)
    return f"""<section class="bg-brand section">
  <div class="container-x grid grid-cols-2 gap-8 lg:grid-cols-4">{cells}</div>
</section>"""


def write(rel, html):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8", newline="\n")
    print("wrote", rel)


# --------------------------------------------------------------------- home
def build_home():
    p = ""
    caps = "".join(f"""<article class="group overflow-hidden rounded-2xl bg-white shadow-sm ring-1 ring-black/5 transition-shadow hover:shadow-xl">
      <div class="aspect-[16/9] overflow-hidden">
        <img src="assets/img/{img}" alt="{name}" loading="lazy" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105">
      </div>
      <h3 class="px-5 py-4 text-base">{name}</h3>
    </article>""" for name, img in CAPABILITIES)

    svc_cards = "".join(f"""<a href="services/{slug}/" class="group flex flex-col overflow-hidden rounded-2xl bg-white shadow-sm ring-1 ring-black/5 transition-shadow hover:shadow-xl">
      <div class="aspect-[16/9] overflow-hidden">
        <img src="assets/img/{img}" alt="{name}" loading="lazy" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105">
      </div>
      <div class="flex flex-1 flex-col p-6">
        <h3 class="text-xl">{name}</h3>
        <p class="mt-3 flex-1 text-sm leading-relaxed">{desc}</p>
        <span class="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-brand group-hover:text-accent-dark">Learn more
          <svg class="h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </span>
      </div>
    </a>""" for slug, name, desc, img in SERVICES)

    html = head(f"{BRAND} - Comprehensive Shipping Solutions",
                "Shreeja Marine Services provides ship and crew management, technical management, "
                "marine insurance, flag documentation and E-Migrate services worldwide.", p)
    html += header(p, "home")
    html += f"""<main id="main">

<section class="relative isolate flex min-h-[88vh] items-center overflow-hidden bg-brand pt-24">
  <img src="assets/img/hero-bg.jpg" alt="" class="absolute inset-0 -z-10 h-full w-full object-cover">
  <div class="absolute inset-0 -z-10 bg-gradient-to-r from-brand via-brand/85 to-brand/40"></div>
  <div class="container-x py-20">
    <div class="max-w-2xl">
      <p class="eyebrow text-accent">Welcome to Shreeja</p>
      <h1 class="mt-4 text-4xl font-extrabold leading-[1.1] text-white sm:text-5xl lg:text-6xl">{BRAND}</h1>
      <p class="mt-6 text-base leading-relaxed text-white/80 sm:text-lg">We provide our services in the ONGC sector, a rising EPC and oil field service provider, active across the full spectrum of the different energy sectors.</p>
      <div class="mt-9 flex flex-col gap-3 sm:flex-row">
        <a href="services/" class="btn-accent">Explore Services</a>
        <a href="contact-us/" class="btn-outline">Contact Us</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container-x grid items-center gap-12 lg:grid-cols-2 lg:gap-16">
    <div class="order-2 lg:order-1">
      <img src="assets/img/about-img.png" alt="Ship's helm at sea" class="w-full rounded-2xl object-cover shadow-lg" loading="lazy">
    </div>
    <div class="order-1 lg:order-2">
      <p class="eyebrow">About Us</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">Dedicated To Excellence</h2>
      <p class="mt-6 leading-relaxed">Shreeja Marine Services was incorporated on 27 Sept 2016. We&rsquo;re India&rsquo;s leading provider of ship &amp; crew management services. Driven by passion and a strong work ethic, we pride ourselves in providing complete end-to-end shipping solutions to ship owners and companies, and helping young aspirants start a successful career in the merchant navy.</p>
      <a href="about-us/" class="btn-accent mt-8">Read more</a>
    </div>
  </div>
</section>

<section class="section bg-mist">
  <div class="container-x">
    <div class="mx-auto max-w-2xl text-center">
      <p class="eyebrow">What We Do</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">We Are Trusted For Our Services</h2>
      <p class="mt-5 leading-relaxed">Fully compliant with the Standards of Training, Certification and Watchkeeping (STCW), we support the industry by delivering high-quality services that ensure operational safety, regulatory adherence, and crew competency.</p>
    </div>
    <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">{caps}</div>
  </div>
</section>

<section class="section">
  <div class="container-x">
    <div class="mx-auto max-w-2xl text-center">
      <p class="eyebrow">Our Services</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">Comprehensive Shipping Solutions</h2>
    </div>
    <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">{svc_cards}</div>
  </div>
</section>

<section class="section bg-mist">
  <div class="container-x">
    <div class="mx-auto max-w-2xl text-center">
      <p class="eyebrow">Why Choose Us</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">We Are The Best And That&rsquo;s Why You Can Choose Us Easily</h2>
      <p class="mt-5 leading-relaxed">With deep industry knowledge and a client-centric approach, the company is equipped to meet the dynamic challenges of the maritime sector, making it a one-stop solution provider for ship owners and operators worldwide.</p>
    </div>
    <div class="mt-14">{highlights_block()}</div>
  </div>
</section>

{stats_block()}

<section class="relative isolate overflow-hidden bg-brand-dark py-20">
  <img src="assets/img/shipment-bg.jpg" alt="" class="absolute inset-0 -z-10 h-full w-full object-cover opacity-25" loading="lazy">
  <div class="container-x text-center">
    <h2 class="mx-auto max-w-3xl text-2xl text-white sm:text-3xl lg:text-4xl">Are You A Shipper? Please Knock Us On The Below Button</h2>
    <div class="mt-9 flex flex-col justify-center gap-3 sm:flex-row">
      <a href="about-us/" class="btn-accent">Know About Company</a>
      <a href="contact-us/" class="btn-outline">Contact Us</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container-x grid gap-12 lg:grid-cols-2 lg:gap-16">
    <div>
      <p class="eyebrow">Quick Quote Price</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">Make Faster Journey to a future that holds surprise for you</h2>
      <p class="mt-5 leading-relaxed">Let&rsquo;s send your query and get a free quote. Join the millions getting bargains on upcoming events, careers and more.</p>
      <ul class="mt-8 space-y-4 text-sm">
        <li class="flex gap-3">{icon('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', 'h-5 w-5 shrink-0 text-accent-dark')}<a href="mailto:{EMAIL}" class="font-semibold text-headline hover:text-accent-dark">{EMAIL}</a></li>
        <li class="flex gap-3">{icon('<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .3 1.9.6 2.8a2 2 0 01-.4 2.1L8.1 9.9a16 16 0 006 6l1.3-1.2a2 2 0 012.1-.4c.9.3 1.8.5 2.8.6a2 2 0 011.7 2z"/>', 'h-5 w-5 shrink-0 text-accent-dark')}<a href="tel:{PHONE_HREF}" class="font-semibold text-headline hover:text-accent-dark">{PHONE}</a></li>
      </ul>
    </div>
    <form action="{FORM_ACTION}" method="POST" class="rounded-2xl bg-mist p-7 ring-1 ring-black/5 sm:p-9">
      <input type="hidden" name="_subject" value="New Quote Request from Shreeja Website">
      <input type="hidden" name="_next" value="https://shreeja.co.in/">
      <input type="hidden" name="_captcha" value="true">
      <input type="hidden" name="_template" value="table">
      <div class="space-y-5">
        <div>
          <label for="q-name" class="mb-2 block text-sm font-semibold text-headline">Your Name</label>
          <input id="q-name" type="text" name="name" required placeholder="Your Name" class="w-full rounded-lg border border-black/10 bg-white px-4 py-3 text-sm outline-none transition focus:border-brand focus:ring-2 focus:ring-brand/20">
        </div>
        <div>
          <label for="q-email" class="mb-2 block text-sm font-semibold text-headline">Email</label>
          <input id="q-email" type="email" name="email" required placeholder="example@email.com" class="w-full rounded-lg border border-black/10 bg-white px-4 py-3 text-sm outline-none transition focus:border-brand focus:ring-2 focus:ring-brand/20">
        </div>
        <div>
          <label for="q-contact" class="mb-2 block text-sm font-semibold text-headline">Contact Number</label>
          <input id="q-contact" type="tel" name="contact" required placeholder="Your Contact Number" class="w-full rounded-lg border border-black/10 bg-white px-4 py-3 text-sm outline-none transition focus:border-brand focus:ring-2 focus:ring-brand/20">
        </div>
        <button type="submit" class="btn-accent w-full">Get a Free Quote</button>
      </div>
    </form>
  </div>
</section>

</main>
"""
    html += footer(p)
    write("index.html", html)


# -------------------------------------------------------------------- about
def build_about():
    p = "../"
    apart = [("Global Standard Compliance", "We strictly adhere to international maritime regulations, safety protocols, and environmental norms."),
             ("Total Customer Support", "Our dedicated service team ensures round-the-clock assistance, transparent communication, and end-to-end coordination throughout the shipping process."),
             ("Strong Global Network", "Strategic alliances with global carriers, port authorities, and logistics partners enable us to offer reliable and competitive solutions worldwide.")]
    items = "".join(f"""<div class="flex gap-5">
      <div class="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-accent font-bold text-brand">{i}</div>
      <div><h3 class="text-lg">{t}</h3><p class="mt-2 text-sm leading-relaxed">{d}</p></div>
    </div>""" for i, (t, d) in enumerate(apart, 1))

    html = head(f"About Us - {BRAND}",
                "Learn about Shreeja Marine Services, India's leading provider of ship and crew "
                "management services since 2016.", p)
    html += header(p, "about")
    html += f"""<main id="main">
{page_hero("About Us", f'<a href="{home(p)}" class="hover:text-accent">Home</a><span>/</span><span class="text-white">About Us</span>', p)}

<section class="section">
  <div class="container-x grid items-center gap-12 lg:grid-cols-2 lg:gap-16">
    <img src="{p}assets/img/about-img.png" alt="Ship's helm at sea" class="w-full rounded-2xl object-cover shadow-lg" loading="lazy">
    <div>
      <p class="eyebrow">Who We Are</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">Dedicated To Excellence</h2>
      <p class="mt-6 leading-relaxed">Shreeja Marine Services was incorporated on 27 Sept 2016. We&rsquo;re India&rsquo;s leading provider of ship &amp; crew management services. Driven by passion and a strong work ethic, we pride ourselves in providing complete end-to-end shipping solutions to ship owners and companies, and helping young aspirants start a successful career in the merchant navy.</p>
      <p class="mt-4 leading-relaxed">From Crew Management and Technical Management to Flag Documentation and E-Migration services for seafarers, Shreeja Marine Services has built a reputation for reliability, efficiency, and customer-centric service. The company caters to a wide range of industries, including oil &amp; gas, manufacturing, retail, automotive, and bulk commodities.</p>
    </div>
  </div>
</section>

{stats_block()}

<section class="section bg-mist">
  <div class="container-x grid gap-12 lg:grid-cols-2 lg:gap-16">
    <div>
      <p class="eyebrow">Our Strengths</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">What Sets Us Apart</h2>
      <p class="mt-5 leading-relaxed">Three things our clients consistently tell us make the difference.</p>
    </div>
    <div class="space-y-8">{items}</div>
  </div>
</section>

<section class="section">
  <div class="container-x">
    <div class="mx-auto max-w-2xl text-center">
      <p class="eyebrow">Why Choose Us</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">Built On Experience</h2>
    </div>
    <div class="mt-14">{highlights_block()}</div>
  </div>
</section>

<section class="bg-brand-dark py-16">
  <div class="container-x flex flex-col items-center justify-between gap-6 text-center lg:flex-row lg:text-left">
    <h2 class="max-w-xl text-2xl text-white sm:text-3xl">Ready to work with a partner you can rely on?</h2>
    <a href="{p}contact-us/" class="btn-accent shrink-0">Contact Us</a>
  </div>
</section>
</main>
"""
    html += footer(p)
    write("about-us/index.html", html)


# ----------------------------------------------------------------- services
def build_services():
    p = "../"
    cards = "".join(f"""<a href="{p}services/{slug}/" class="group flex flex-col overflow-hidden rounded-2xl bg-white shadow-sm ring-1 ring-black/5 transition-shadow hover:shadow-xl">
      <div class="aspect-[16/9] overflow-hidden">
        <img src="{p}assets/img/{img}" alt="{name}" loading="lazy" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105">
      </div>
      <div class="flex flex-1 flex-col p-6">
        <h3 class="text-xl">{name}</h3>
        <p class="mt-3 flex-1 text-sm leading-relaxed">{desc}</p>
        <span class="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-brand group-hover:text-accent-dark">Learn more
          <svg class="h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </span>
      </div>
    </a>""" for slug, name, desc, img in SERVICES)

    html = head(f"Our Services - {BRAND}",
                "Technical management, crew management, marine insurance, E-Migrate and flag "
                "documentation services from Shreeja Marine Services.", p)
    html += header(p, "services")
    html += f"""<main id="main">
{page_hero("Our Services", f'<a href="{home(p)}" class="hover:text-accent">Home</a><span>/</span><span class="text-white">Services</span>', p)}
<section class="section">
  <div class="container-x">
    <div class="mx-auto max-w-2xl text-center">
      <p class="eyebrow">What We Offer</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">Comprehensive Shipping Solutions</h2>
      <p class="mt-5 leading-relaxed">End-to-end support for ship owners and operators worldwide, delivered by a team with over a decade of maritime experience.</p>
    </div>
    <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">{cards}</div>
  </div>
</section>
<section class="bg-brand-dark py-16">
  <div class="container-x flex flex-col items-center justify-between gap-6 text-center lg:flex-row lg:text-left">
    <h2 class="max-w-xl text-2xl text-white sm:text-3xl">Not sure which service you need? Talk to our team.</h2>
    <a href="{p}contact-us/" class="btn-accent shrink-0">Get in Touch</a>
  </div>
</section>
</main>
"""
    html += footer(p)
    write("services/index.html", html)


def build_service_detail(slug, name, desc, img):
    p = "../../"
    intro, bullets = SERVICE_DETAIL[slug]
    lis = "".join(f"""<li class="flex gap-4 rounded-xl bg-white p-5 shadow-sm ring-1 ring-black/5">
      <span class="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-accent text-brand">
        <svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>
      </span>
      <span><strong class="block text-headline">{t}</strong><span class="mt-1 block text-sm leading-relaxed">{d}</span></span>
    </li>""" for t, d in bullets)

    others = "".join(f'<a href="{p}services/{s}/" class="rounded-full bg-white px-5 py-2.5 text-sm font-semibold text-brand ring-1 ring-black/10 transition-colors hover:bg-brand hover:text-white">{n}</a>'
                     for s, n, _, _ in SERVICES if s != slug)

    html = head(f"{name} - {BRAND}", desc, p)
    html += header(p, "services")
    html += f"""<main id="main">
{page_hero(name, f'<a href="{home(p)}" class="hover:text-accent">Home</a><span>/</span><a href="{p}services/" class="hover:text-accent">Services</a><span>/</span><span class="text-white">{name}</span>', p)}

<section class="section">
  <div class="container-x grid gap-12 lg:grid-cols-2 lg:gap-16">
    <div>
      <img src="{p}assets/img/{img}" alt="{name}" class="w-full rounded-2xl object-cover shadow-lg" loading="lazy">
    </div>
    <div>
      <p class="eyebrow">Service</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">{name}</h2>
      <p class="mt-6 leading-relaxed">{intro}</p>
    </div>
  </div>
</section>

<section class="section bg-mist pt-0">
  <div class="container-x">
    <h2 class="text-2xl sm:text-3xl">What&rsquo;s Included</h2>
    <ul class="mt-8 grid gap-4 sm:grid-cols-2">{lis}</ul>
  </div>
</section>

<section class="section">
  <div class="container-x">
    <h2 class="text-2xl sm:text-3xl">Other Services</h2>
    <div class="mt-6 flex flex-wrap gap-3">{others}</div>
  </div>
</section>

<section class="bg-brand-dark py-16">
  <div class="container-x flex flex-col items-center justify-between gap-6 text-center lg:flex-row lg:text-left">
    <h2 class="max-w-xl text-2xl text-white sm:text-3xl">Need {name.lower()} support for your fleet?</h2>
    <a href="{p}contact-us/" class="btn-accent shrink-0">Contact Us</a>
  </div>
</section>
</main>
"""
    html += footer(p)
    write(f"services/{slug}/index.html", html)


# ------------------------------------------------------------------ contact
def build_contact():
    p = "../"
    maps = ("https://www.google.com/maps?q=" +
            "NBC+Complex,+Sector+11,+CBD+Belapur,+Navi+Mumbai,+Maharashtra+400614&output=embed")
    cards = [("Email Us", f'<a href="mailto:{EMAIL}" class="font-semibold text-headline transition-colors hover:text-accent-dark">{EMAIL}</a>',
              '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'),
             ("Call Us", f'<a href="tel:{PHONE_HREF}" class="font-semibold text-headline transition-colors hover:text-accent-dark">Tel. {PHONE}</a>',
              '<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .3 1.9.6 2.8a2 2 0 01-.4 2.1L8.1 9.9a16 16 0 006 6l1.3-1.2a2 2 0 012.1-.4c.9.3 1.8.5 2.8.6a2 2 0 011.7 2z"/>'),
             ("Navi Mumbai", f'<span class="text-sm leading-relaxed">{ADDRESS}</span>',
              '<path d="M12 21s7-5.5 7-11a7 7 0 10-14 0c0 5.5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>')]
    info = "".join(f"""<div class="rounded-2xl bg-white p-7 shadow-sm ring-1 ring-black/5">
      <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-brand text-accent">{icon(ic)}</div>
      <h3 class="mt-5 text-lg">{t}</h3>
      <div class="mt-2">{v}</div>
    </div>""" for t, v, ic in cards)

    field = ('w-full rounded-lg border border-black/10 bg-white px-4 py-3 text-sm outline-none '
             'transition focus:border-brand focus:ring-2 focus:ring-brand/20')

    html = head(f"Contact Us - {BRAND}",
                f"Get in touch with Shreeja Marine Services. Email {EMAIL} or call {PHONE}.", p)
    html += header(p, "contact")
    html += f"""<main id="main">
{page_hero("Contact Us", f'<a href="{home(p)}" class="hover:text-accent">Home</a><span>/</span><span class="text-white">Contact Us</span>', p)}

<section class="section bg-mist">
  <div class="container-x grid gap-6 sm:grid-cols-2 lg:grid-cols-3">{info}</div>
</section>

<section class="section">
  <div class="container-x grid gap-12 lg:grid-cols-2 lg:gap-16">
    <div>
      <p class="eyebrow">Get In Touch</p>
      <h2 class="mt-3 text-3xl sm:text-4xl">Send Us a Message</h2>
      <p class="mt-5 leading-relaxed">Tell us what you need and our team will get back to you as soon as possible.</p>
      <div class="mt-8 overflow-hidden rounded-2xl shadow-lg ring-1 ring-black/5">
        <iframe title="Shreeja Marine Services office location" src="{maps}" width="100%" height="320" style="border:0" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
    <form action="{FORM_ACTION}" method="POST" class="rounded-2xl bg-mist p-7 ring-1 ring-black/5 sm:p-9">
      <input type="hidden" name="_subject" value="New Contact Enquiry from Shreeja Website">
      <input type="hidden" name="_next" value="https://shreeja.co.in/">
      <input type="hidden" name="_captcha" value="true">
      <input type="hidden" name="_template" value="table">
      <div class="grid gap-5 sm:grid-cols-2">
        <div>
          <label for="c-name" class="mb-2 block text-sm font-semibold text-headline">Name</label>
          <input id="c-name" type="text" name="name" required placeholder="Name" class="{field}">
        </div>
        <div>
          <label for="c-email" class="mb-2 block text-sm font-semibold text-headline">Email</label>
          <input id="c-email" type="email" name="email" required placeholder="Email" class="{field}">
        </div>
        <div>
          <label for="c-phone" class="mb-2 block text-sm font-semibold text-headline">Phone</label>
          <input id="c-phone" type="tel" name="phone" placeholder="Phone" class="{field}">
        </div>
        <div>
          <label for="c-subject" class="mb-2 block text-sm font-semibold text-headline">Subject</label>
          <input id="c-subject" type="text" name="subject" placeholder="Subject" class="{field}">
        </div>
        <div class="sm:col-span-2">
          <label for="c-message" class="mb-2 block text-sm font-semibold text-headline">Message</label>
          <textarea id="c-message" name="message" rows="5" required placeholder="Message" class="{field}"></textarea>
        </div>
        <div class="sm:col-span-2">
          <button type="submit" class="btn-accent w-full">Send</button>
        </div>
      </div>
    </form>
  </div>
</section>
</main>
"""
    html += footer(p)
    write("contact-us/index.html", html)


if __name__ == "__main__":
    build_home()
    build_about()
    build_services()
    for slug, name, desc, img in SERVICES:
        build_service_detail(slug, name, desc, img)
    build_contact()
    print("\nDone.")
