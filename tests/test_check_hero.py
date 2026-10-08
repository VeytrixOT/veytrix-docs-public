import unittest

from scripts.check_hero import validate_html


class HeroStructureTests(unittest.TestCase):
    def test_valid_hero(self) -> None:
        validate_html(
            '<div class="veytrix-hero"><div class="veytrix-hero__content">'
            "<h1>Welcome</h1></div>"
            '<div class="veytrix-hero__diagram">Diagram</div></div>'
        )

    def test_rejects_flattened_hero(self) -> None:
        with self.assertRaisesRegex(ValueError, "unexpected hero child structure"):
            validate_html(
                '<div class="veytrix-hero"><h1>Welcome</h1>'
                '<div class="veytrix-hero__diagram">Diagram</div></div>'
            )

    def test_rejects_missing_heading(self) -> None:
        with self.assertRaisesRegex(ValueError, "missing its h1"):
            validate_html(
                '<div class="veytrix-hero"><div class="veytrix-hero__content">'
                "No heading</div>"
                '<div class="veytrix-hero__diagram">Diagram</div></div>'
            )

    def test_void_self_closing_tag_does_not_pop_content(self) -> None:
        validate_html(
            '<div class="veytrix-hero"><div class="veytrix-hero__content">'
            "<br/><img src=\"mark.svg\"/>"
            "<h1>Welcome</h1></div>"
            '<div class="veytrix-hero__diagram">Diagram</div></div>'
        )


if __name__ == "__main__":
    unittest.main()
