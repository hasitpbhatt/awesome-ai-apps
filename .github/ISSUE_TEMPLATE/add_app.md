---
name: App submission
description: Propose a new AI app for the awesome-ai-apps list
title: "[App] <App Name>"
labels: ["app submission"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Thanks for contributing. Check the README first — the app must not already be listed, and every entry must be a verified, one-line description placed alphabetically in one of the 10 categories.
  - type: input
    id: app-name
    attributes:
      label: App name
      description: Exact name as it should appear in the list.
      placeholder: e.g. ChatGPT
    validations:
      required: true
  - type: input
    id: app-url
    attributes:
      label: Official link
      description: Official website or primary repository URL (no affiliate or referral links).
      placeholder: https://example.com
    validations:
      required: true
  - type: input
    id: description
    attributes:
      label: One-line description
      description: A single factual sentence, matching the tone of existing entries (see README).
      placeholder: e.g. Does X for Y with feature Z.
    validations:
      required: true
  - type: dropdown
    id: category
    attributes:
      label: Category
      description: The category this app best fits (see README Contents).
      options:
        - AI Chatbots
        - AI Coding
        - AI Search & Research
        - AI Writing
        - AI Image
        - AI Video
        - AI Audio & Voice
        - AI Productivity & Knowledge
        - AI Automation & Agents
        - Local & Open Source
    validations:
      required: true
  - type: textarea
    id: why
    attributes:
      label: Why does it stand out?
      description: Briefly explain what makes this app genuinely stand out vs. existing entries. This keeps the list lean — only apps that truly impress get included.
    validations:
      required: true
  - type: checkboxes
    id: checks
    attributes:
      label: Checklist
      options:
        - label: The app is not already listed in the README
          required: true
        - label: The link is verified and points to the official product
          required: true
        - label: The description is a single factual sentence (no hype or marketing copy)
          required: true
