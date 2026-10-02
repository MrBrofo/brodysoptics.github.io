# Brodysoptics: photography portfolio site

This is Brody Disick's photography portfolio and booking site. Read this whole file before making changes.

- **Live site:** https://brodysoptics.com (www.brodysoptics.com is the main custom domain)
- **Repo:** `MrBrofo/brodysoptics.github.io` (GitHub Pages, deploys from `main`, root folder)
- **Fallback URL:** mrbrofo.github.io/brodysoptics.github.io
- **Owner:** Brody Disick. Brand name: **Brodysoptics.** (with the period)

---

## Working with Brody

- Talk casually and directly. Explain things plainly; he isn't a developer.
- **Make small, targeted changes.** He iterates one tweak at a time. Don't rewrite or restyle things he didn't ask about.
- When a request is ambiguous (e.g. which "Work" text), change the most likely one and mention the other.
- Give honest opinions when asked (e.g. pricing, design). Push back kindly if something will cause problems.
- After changes, tell him briefly what changed. He deploys by committing + pushing (he uses GitHub Desktop; you can also commit/push for him if he asks).
- Test layout changes at desktop (~1300px) and phone (~390px) widths.

---

## Files

```
index.html     ← the entire site (HTML + CSS + JS, no build step, no frameworks)
CNAME          ← keeps brodysoptics.com connected. NEVER delete or edit.
CLAUDE.md      ← this file
favicon.png    ← "B." tab icon + iPhone home-screen icon (180×180)
preview.jpg    ← link-preview picture for texts/socials (1200×630, og:image). Keep it OUT of photos/ or it shows as a single photo.
photos/        ← all images and videos (see rules below)
```

Everything Brody normally wants to change is in the `SITE` object at the top of `index.html`. Prefer editing there over hardcoding.

### The SITE settings object
- `look`: color style: `"darkroom"` (current), `"kodak"`, `"nightgame"`
- `brand`: `"Brodysoptics."` (top-left signature logo + giant footer wordmark; browser tab strips the period)
- `name`: `"Brody Disick"` (shown over the hero photo)
- `tagline`: `""` (empty = hidden; he removed it on purpose)
- `instagram`: `""` (empty = hidden)
- `githubUser`: `"MrBrofo"`, `githubRepo`: `"brodysoptics.github.io"`, `githubBranch`: `"main"`
- `googleFormId` + `formEntries`: booking form wiring (see below)
- `pricing`: array of packages (see below)

---

## Photos and videos

The site finds media automatically via the GitHub API (`/repos/MrBrofo/brodysoptics.github.io/git/trees/main?recursive=1`). No code changes are needed to add photos.

- `photos/hero.jpg` = big top image. Matches any name starting with "hero" (e.g. `hero (Web).jpg`, `HERO.JPG`). Must be a photo, not a video.
- `photos/<Album Name>/...` = one album per folder. Folder name = album title shown on the site.
- `cover.jpg` (or `cover (Web).jpg`) inside an album = its cover. Otherwise the first photo is used (never a video if a photo exists).
- Loose files directly in `photos/` (not hero) = single photos, shown after albums on the My Work page.
- Supported: `.jpg .jpeg .png .webp .avif` and videos `.mp4 .webm .mov .m4v` (recommend MP4/H.264; some iPhone HEVC .mov won't play in Chrome).
- Order = filename order (numeric-aware), so `01.jpg, 02.jpg...` controls order.
- Each album gets its own link: `#album/Album-Name` (spaces become dashes).

**File size guidance (Brody asks about this):**
- Photos: ~1 MB each, max ~1.5 MB. Export 2500px long edge, JPEG quality ~80–85. Hero ideally under 1 MB.
- He resizes with **PowerToys Image Resizer** (preset "Web": 2500×2500, Fit, JPEG quality 85), which names files `name (Web).jpg`.
- Videos: 1080p, under ~50 MB. GitHub rejects files over 100 MB. Long videos should go on YouTube.
- GitHub Pages wants the whole repo under ~1 GB.

---

## Site sections (top to bottom)

1. **Nav** (fixed): signature logo "Brodysoptics." left; links "My Work", "Pricing", "Book" + Instagram icon right (on phones ≤420px the logo/menu shrink slightly so it all fits on one line). He wants people to use the booking form, not DM, so don't add "DM me" prompts. Goes solid/frosted just before it would overlap the hero name.
2. **Hero:** full-bleed hero photo with slow zoom-in. It's **pinned** (`position:sticky`, z-index -3) and the rest of the page slides up over it like a sheet (`main::before`/`footer::before` paint the page background at z -2; the `#field` slashes canvas is z -1 and clipped so it never draws on the hero). Nav goes solid when `#work` reaches it. The hero fades out as you scroll (`heroFade()`: opacity 1 → 0 by the time it's covered). The old scroll parallax was removed for this; "BRODY DISICK" in smaller uppercase (clamp(2.2rem,5vw,4rem)) at bottom left, words slide up on load. No tagline.
3. **My Work:** heading "MY WORK". Grid of album covers (4:5) then singles.
4. **Pricing:** clickable price list.
5. **Book a shoot:** inquiry form.
6. **Footer:** giant "BRODYSOPTICS." wordmark ("OPTICS." in sunset gradient, auto-fit to width), © line.

**There is no About section.** He removed it on purpose. Don't add it back.

### My Work grid
- Tiles are 4:5 with film-frame numbers (01, 02…). Album tiles show title + count ("10 photos · 2 videos") on hover (always visible on touch devices). Hover = slight zoom + viewfinder corner brackets.
- `fitCols()` picks the column count so there's **never a lone tile in the last row**. He specifically asked for complete rows.

### Album pages
- Header: "‹ All work" link, album title, count.
- Photos laid out in **balanced justified rows** (`partition()` + `layoutAlbum()`): every row is full width, every photo in a row is the same height, photos keep their real shape (no cropping). Modeled on Adobe Portfolio. Relayouts on resize and as images load.
- Videos show the first frame + play icon, hover = muted preview, click = viewer with controls.
- Below the photos: **"CHECK OUT MY OTHER WORK"** with the other albums as smaller tiles (`.tiles.small`, `data-size="200"`), then a **"← BACK TO HOMEPAGE"** button.
- Inside albums, **Pricing and Book sections and their nav links are hidden** (`body.in-album`). Pricing/form only appear on the main page.

### Viewer (lightbox)
- Full-screen dialog; prev/next buttons, arrow keys, swipe; fades between items; supports video.

---

## Pricing (current)

| Name | Shown as | Google Form value | Price | Details |
|---|---|---|---|---|
| Basic | Basic | Basic | $25 | ~15 edited photos |
| Standard | Standard | Standard | $40 | ~30 edited photos |
| Full | Full + "BEST VALUE" badge | Full | $45 | ~45 edited photos |
| Group / team | Group / team | Group/Team | $20 per person | 3 or more people, at least 5 edited photos each |
| Video edit | Video edit | Video (Mixtape/edit) | $50 | A 30 second to 1 minute highlight video cut to music |

The list is split into categories with `{ group: "..." }` rows: **Sports** (the table above), **Portraits** (Portrait session $40 = 1 hour ~12 edited photos; Extended portrait session $100 = 3 hours ~35 edited photos, "time for outfit and location changes" (not "room", which sounds like a physical room); both have `other: true`, so they're sent through the Google Form's "Other" package option), **Events** (From $25/hour, ~15–20 edited photos per hour) and **Graphics** (Single post from $10, Season template set from $40). Each row's optional `path` ("Photo" default, "Video", "Graphic Design") says which booking path clicking it starts. Photo rows without `form` use `SITE.customPackage` ("Not sure / custom"); `subject` pre-fills "What's it for?"; `graphic` pre-picks the graphic kind.

Decisions behind this:
- Standard is $40 on purpose (decoy pricing to nudge people to Full at $45).
- Badge says **"Best value"**, not "Most popular".
- Use "~" not "About".
- No "prices are starting points" note (removed).
- Group / team: no "plus group shots" (removed).
- He decided **not** to offer unedited/raw photos with any package.
- He's keeping prices low to build a clientele.

Clicking a pricing row: starts the booking form on that row's path with the package pre-picked, skips to "What's your name?", makes the form card glow, smooth-scrolls to it. "BOOK THIS →" shows on hover (always on touch).

---

## Booking form → Google Form

The site form posts directly into Brody's Google Form (responses land in his linked Google Sheet). It uses a `no-cors` POST to:
`https://docs.google.com/forms/d/e/1FAIpQLSeVEzIjqwg7Fcim7Z5hEXjT3fplNuXDySzg26LP9XgUlmt7zQ/formResponse`

The form is **one question at a time** (`QUESTIONS` array in the script, rendered into `form#form.wiz`): progress bar, "Question X of N", choices are pill buttons that auto-advance, Back/Next, Enter = Next. Question 1 "What are you after?" picks a path and only that path's questions are sent:
- **Photo:** name, what's it for, package, where, date/time, orientation, posting, referral, contact (method + handle), anything else
- **Video:** name, what's it for, kind of video, where, date/time, posting, referral, contact, anything else
- **Graphic Design:** name, what's it for, kind of graphic, need-by date, posting, referral, contact, anything else

No "mix" path (Brody decided against it). In the Google Form only name + "What do you want?" are Required; everything else must stay optional or responses from other paths get dropped.

Entry IDs (`SITE.formEntries`):
- name `1690814314`, what `1249857742`
- package `1485016801`, videoKind `2116150638`, graphicKind `183670750`
- subject `49302972` (what's it for), location `2146188724`, datetime `1012313159`, needBy `1146888609`
- orientation `1308545335`, contactMethod `1162604422`, contact `729877922`
- posting `1602938962`, referral `921430376` (free text), other `1182973985`

**Multiple-choice values must match the Google Form EXACTLY or Google silently drops the whole response:**
- What: `Photo`, `Video`, `Graphic Design` (shown as Photos / Video / highlight reel / Graphics)
- Package: `Basic`, `Standard`, `Full`, `Group/Team`, `Video (Mixtape/edit)`, plus "Not sure / custom" sent through the form's **Other** option (`__other_option__` + `entry.ID.other_option_response`)
- Video kind: `Season highlight reel`, `Single-game highlights`, `Hype video`, `Intro Video`, `Event Recap`, `Clips for social media (vertical)`
- Graphic kind: `Gameday/Matchup`, `Commitment/Recruiting`, `Score/recap`, `Full season template set`, plus "Something else" through **Other**
- Orientation: `Vertical`, `Horizontal`, `Both`, `Either or, I don't care` (shown as "Either, I don't care")
- Posting: `Yes!`, `No thanks`, `I dont care` (no apostrophe in the Google Form; shown as "I don't care")
- `VIA_OTHER` in the script lists which answers go through "Other".

If Brody renames anything in the Google Form, update the site to match. To get new entry IDs: Google Form → ⋮ → Get pre-filled link → fill every question → Get link; the `entry.NNN` params are in question order.

Because it's `no-cors`, the site always shows "Inquiry sent" even if Google rejects it. The real test is checking the Google Form's Responses tab / Sheet.

Intro line above the form: "Answer a few quick questions and I'll get back to you as soon as I can!"

---

## Design system

- **Look "darkroom"** (current): background `#0E0D0C`, text `#F2EEE8`, muted `#9A938A`, lines `#2B2825`, accent `#F4895F` (soft sunset orange), sunset gradient `#F7B267 → #F4845F → #E8687F`. Brody asked for "sunset, not harsh", so don't go back to a harsh red.
- Other looks exist (`kodak` = off-white + yellow, `nightgame` = navy + orange) via `:root[data-look=...]`.
- Fonts (Google Fonts):
  - **Archivo** (condensed via `font-stretch`, heavy, UPPERCASE) for headings and UI
  - **Newsreader** serif for body text
  - **Herr Von Muellerhoff** for the signature logo (write-on clip-path animation)
- Subtle film-grain overlay over the page (`body::after`).
- Mouse field (`#field` canvas, `SITE.mouseField`): faint grid of "/" slashes behind the content; near the cursor they turn away, push out and glow in the accent color. Computers only, off for reduced motion. The slashes scroll with the page (grid is in page coordinates, state kept per row/column). Layering is explained under Hero (it sits between the page background and the content). Stays calm over the hero, album photos, price list and form.
- Animations: scroll reveal (`.rv` → `.in` via IntersectionObserver), hero zoom + word rise, parallax, frosted sticky nav, lightbox fades. All disabled under `prefers-reduced-motion`.
- Rejected directions: the original gray/blue "corporate" palette felt boring/corporate. He wants it to feel personal, not like a company site.

---

## Hosting / domain setup (already done)

- GitHub Pages: Settings → Pages → Deploy from a branch → `main` / root. Custom domain `www.brodysoptics.com`. Enforce HTTPS once the certificate is issued.
- Domain registered/DNS on **Cloudflare**. Records (all **DNS only / grey cloud**, TTL Auto; proxy must stay off or GitHub HTTPS breaks):
  - A `@` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
  - CNAME `www` → `mrbrofo.github.io`
- Cloudflare warns about no email/MX/SPF. Suggested fix: Cloudflare Email Routing (e.g. hello@brodysoptics.com → his Gmail). Not confirmed as done.

## Deploying

- Brody uses **GitHub Desktop**: edit files in the cloned folder → Summary → Commit to main → Push origin. Site updates in ~1–2 minutes (check the repo's Actions tab for "pages build and deployment").
- The GitHub website upload limit is 25 MB/file and 100 files per upload. GitHub Desktop avoids that (100 MB/file hard limit).

## Business notes (context, not code)

- Payments: suggested Venmo/Zelle, a small deposit to lock the date, the rest before delivering the full gallery, delivery via Google Drive, tracking payments in the form's Google Sheet. Not on the site yet; he may ask to add a line like "A small deposit locks in your date. Venmo and Zelle accepted."

## Possible future requests
- YouTube embeds for longer videos inside albums.
- Replacing the signature-font logo with his real handwritten signature (trace a photo of it into SVG, keep the write-on animation).
- Adding his Instagram (set `SITE.instagram`).
