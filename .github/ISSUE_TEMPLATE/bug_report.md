---
name: Bug report
description: Report a problem with the repo, a broken link, or an incorrect entry
title: "[Bug] <Short summary>"
labels: ["bug"]
assignees: []
body:
  - type: textarea
    id: what
    attributes:
      label: What happened?
      description: Describe the issue clearly. Include the app name and category if this is about a README entry.
      placeholder: e.g. The link for <App Name> in <Category> no longer works / the description is wrong.
    validations:
      required: true
  - type: input
    id: location
    attributes:
      label: Where does it occur?
      description: README section (category) or the file/line involved.
      placeholder: e.g. AI Coding section, line 42
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
      description: What should happen instead?
      placeholder: e.g. The link should point to the current official site.
  - type: dropdown
    id: severity
    attributes:
      label: Severity
      options:
        - Broken link
        - Incorrect description
        - Wrong category
        - Formatting / alphabetical order
        - Other
    validations:
      required: true
  - type: input
    id: environment
    attributes:
      label: Environment (if applicable)
      description: OS, browser, or tool versions.
      placeholder: e.g. Windows 11, Chrome 126
  - type: textarea
    id: steps
    attributes:
      label: Steps to reproduce (if applicable)
      description: How did you run into this?
      placeholder: 1. Open README 2. Click the link 3. See 404
