# 30-Day Growth Calendar

**Launch date: Tuesday, August 4, 2026, ~09:30 AM US Eastern** (HN traffic peaks Tue–Thu mornings; Tuesday morning maximizes comment visibility through the week).

All actions are value-first. The calendar is built around **responding, helping, and improving** — not repeated self-promotion. Days 1–4 carry the posting load; the rest is compounding.

---

## Phase 0 — Pre-launch (Aug 1–3, done before Day 1)

- [ ] Re-verify all 127 links; fix any dead ones in the same PR.
- [ ] Add a "Verified" / last-verified note to the README if it's not there yet.
- [ ] Make a clean screenshot of the README (table of contents view) for any image-friendly subs.
- [ ] Confirm the GitHub repo is public, description is set, and topics are tagged (`awesome-list`, `ai`, `llm`, `artificial-intelligence`).
- [ ] Set up tracking (see "Tracking" section at the end).

---

## Phase 1 — Launch week (Days 1–7)

### Day 1 — Tue, Aug 4: Show HN launch
- Submit Show HN (`promo/show-hn-post.md`) at ~09:30 ET. Use the exact title from the file.
- Paste the body as the first comment within the first minute (essential — bare submissions get flagged).
- Stay in the thread for the first 2 hours replying to every comment.
- Post links to the repo in replies only where directly relevant.

### Day 2 — Wed, Aug 5: Morning HN sweep + first Reddit post
- AM: Reply to every overnight HN comment. Answer the prepared HN criticisms from `promo/hacker-news-comments.md` where they match.
- ~12:00 ET: Post to **r/InternetIsBeautiful** (`promo/reddit-posts.md` #3). Reply to every comment through the afternoon.

### Day 3 — Thu, Aug 6: Second Reddit post
- AM: Check HN again; keep the top threads alive.
- ~12:00 ET: Post to **r/artificial** (`promo/reddit-posts.md` #1). Its audience is the most critical — engage deeply, don't defend, agree and fix.

### Day 4 — Fri, Aug 7: Third Reddit post
- AM: Answer new comments on r/artificial.
- ~10:00 ET: Post to **r/OpenAI** (`promo/reddit-posts.md` #2).
- PM: Note every piece of feedback across all platforms in one file (`promo/feedback-log.md` or an issue thread). Turn the top 3 into repo improvements by Sunday.

### Day 5 — Sat, Aug 8: No posting. Rest and respond.
- Reply to all weekend comments on every post.
- Do a **repo improvement pass**: fix the top 3 issues raised this week.

### Day 6 — Sun, Aug 9: Silent maintenance
- Reply to stragglers. No new posts.
- If any Reddit post got ratio'd, read *why* honestly. Adjust the pitch for future weeks.
- Update the README stats line if apps were added/changed.

### Day 7 — Mon, Aug 10: Week-one recap (internal only)
- Measure week 1 (stars, traffic, top referrers — see Tracking).
- Post a short **update comment on the Show HN thread** if there's real news (e.g., "Added 3 apps people suggested, fixed 2 dead links — thanks everyone"). Only if it's true and the thread is still active.
- Thank each contributor who opened a PR with a real reply (not a bot message).

---

## Phase 2 — Consolidation (Days 8–21): no posting, all contributing

### Day 8 — Tue, Aug 11
- Reply to remaining Reddit/HN comments (keep reply debt at zero).

### Day 9 — Wed, Aug 12
- Contribute a *genuine answer* (not a pitch) to 2 relevant HN discussions in the AI space. The repo may come up naturally in one of them.

### Day 10 — Thu, Aug 13
- Reply to one "what AI tool should I use for X?" thread — recommend the 1–2 best fits from the list, link only if it genuinely helps.

### Day 11 — Fri, Aug 14
- Check for dead links flagged this week; fix same-day.
- Prepare the cross-listing pitch (from the community-manager plan) for Monday.

### Day 12 — Sat, Aug 15
- No promotion. Fix any low-hanging repo issues; merge pending PRs.

### Day 13 — Sun, Aug 16
- No promotion. Reply to comments. Keep the contribution pipeline clean.

### Day 14 — Mon, Aug 17
- **Cross-listing outreach #1:** Open PRs / submit forms to the top 3 awesome lists and directories from `promo/cross-listing-plan.md`. Draft each submission specifically for that list (no copy-paste).

### Day 15 — Tue, Aug 18
- Answer comments. Do a 2nd dead-link sweep pass.

### Day 16 — Wed, Aug 19
- Genuine engagement: answer 2–3 AI questions on r/artificial and r/OpenAI that are *unrelated to the list*. Build the account as a helpful member, not a promoter.

### Day 17 — Thu, Aug 20
- Follow up on cross-listing submissions that went unanswered (7 days later). Politely nudge once.

### Day 18 — Fri, Aug 21
- Merge pending PRs. If a contributor milestone happened this week, celebrate it in the repo (not on socials).

### Day 19 — Sat, Aug 22
- No promotion. Reply to comments.

### Day 20 — Sun, Aug 23
- No promotion. Two-week retrospective (internal): what gained traction, what didn't.

### Day 21 — Mon, Aug 24
- **Cross-listing outreach #2:** Second wave of lists/directories that accept rolling submissions.

---

## Phase 3 — Sustain (Days 22–30): become a recurring resource

### Day 22 — Tue, Aug 25
- Reply to comments; merge PRs. Announce merged PRs in commit messages.

### Day 23 — Wed, Aug 26
- Newsletter outreach #1: reply to / pitch 2–3 small, niche AI newsletters (e.g., weekly AI tool roundups) with the list as a *reference*, one personalized line each. No blast email.

### Day 24 — Thu, Aug 27
- Answer comments on the existing Reddit posts (they'll have faded; keep replies current anyway).

### Day 25 — Fri, Aug 28
- Content pass: if the README needs a new category or a reorganization, do it now and mention it in the commit log.

### Day 26 — Sat, Aug 29
- No promotion. Reply to comments.

### Day 27 — Sun, Aug 30
- No promotion. Fix anything that aged this month (dead links, outdated descriptions).

### Day 28 — Mon, Aug 31
- **Monthly update post:** on r/artificial or r/OpenAI (whichever performed best), a value post that *happens* to mention the list: "I maintain a 127-app AI list — here's what changed this month, and the tools people keep requesting." Lead with learnings, not the link.

### Day 29 — Tue, Sep 1
- Reply to all comments on the monthly update post. Re-check tracking.

### Day 30 — Wed, Sep 2
- **Wrap-up:** measure the full 30 days. Post a final update comment on the Show HN thread (only if something real changed: contributor count, new apps, cross-listings).
- Decide the ongoing rhythm: e.g., monthly update post + weekly engagement, indefinitely. Write it down so the calendar isn't a one-shot.

---

## Tracking

Track **stars and traffic**, not vanity:

- **Stars:** GitHub API — `https://api.github.com/repos/<owner>/awesome-ai-apps` → check `stargazers_count` daily (same time, log in a `docs/stars.csv` or spreadsheet). Watch the *shape* (spike on Day 1–4, steady crawl after) more than the number.
- **Traffic:** GitHub repo → Insights → Traffic (views + unique visitors + top referrers). Referrers tell you which channel worked: expect `news.ycombinator.com` and `reddit.com` early.
- **Repo use:** fork count, clone count, and PR volume are better health signals than stars. Track PRs opened/merged per week.
- **Which posts convert:** compare referral spikes against each post's date. Double down on the channel that sends real visitors, not the one that just feels active.
- **Watch the ratio:** engagement (comments, replies) vs. downvotes tells you if a post read as spam. If any sub flagged it, learn and don't repeat the pattern.

### Health rules
- Never post the same content to more than one sub in a day.
- Never post without replying for the next 48h.
- Never DM the link.
- If a community says "this is spam," believe them and stop that channel — the list survives on trust, not reach.
