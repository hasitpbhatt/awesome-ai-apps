import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
CONTRIBUTING = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
APP_ENTRY = re.compile(r"^- \*\*\[([^\]]+)\]\([^)]+\)\*\*:", re.MULTILINE)
EXCLUDED_HEADINGS = {"Contents", "Contributing", "License"}


def readme_categories_and_entries():
    categories = []
    entries = {}
    current_category = None

    for line in README.splitlines():
        heading = re.match(r"^## (.+)$", line)
        if heading:
            current_category = heading.group(1)
            if current_category not in EXCLUDED_HEADINGS:
                categories.append(current_category)
                entries[current_category] = []
            continue

        if current_category in entries:
            app = APP_ENTRY.match(line)
            if app:
                entries[current_category].append(app.group(1))

    return categories, entries


class ReadmeTests(unittest.TestCase):
    def test_summary_counts_match_list(self):
        categories, entries = readme_categories_and_entries()
        summary = re.search(
            r"\*\*Total: (\d+) AI apps across (\d+) categories\*\*", README
        )
        self.assertIsNotNone(summary, "README summary line is missing or malformed")
        self.assertEqual(int(summary.group(1)), sum(map(len, entries.values())))
        self.assertEqual(int(summary.group(2)), len(categories))

    def test_contributing_counts_and_categories_match_readme(self):
        categories, entries = readme_categories_and_entries()
        summary = re.search(
            r"\*\*(\d+) hand-picked AI apps across (\d+) categories\*\*",
            CONTRIBUTING,
        )
        self.assertIsNotNone(summary, "Contributing summary is missing or malformed")
        self.assertEqual(int(summary.group(1)), sum(map(len, entries.values())))
        self.assertEqual(int(summary.group(2)), len(categories))

        table_categories = re.findall(
            r"^\s*\|\s*\d+\s*\|\s*(.*?)\s*\|$", CONTRIBUTING, re.MULTILINE
        )
        self.assertEqual(table_categories, categories)

    def test_entries_are_alphabetical_within_categories(self):
        _, entries = readme_categories_and_entries()
        for category, names in entries.items():
            with self.subTest(category=category):
                self.assertEqual(names, sorted(names, key=str.casefold))


if __name__ == "__main__":
    unittest.main()