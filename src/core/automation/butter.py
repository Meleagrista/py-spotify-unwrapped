import os
import re
import subprocess

from playwright.sync_api import sync_playwright, Page

from src.constants import SESSION_FILE, DOWNLOAD_DIR, PLAYWRIGHT_START_URL


def ensure_browsers_installed():
    try:
        subprocess.run(["playwright", "install", "chromium"], check=True)
    except Exception as e:
        print("Failed to install browsers:", e)
        exit(1)

def generate_login_session():
    ensure_browsers_installed()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--headless=new"])
        context = browser.new_context()
        page = context.new_page()
        page.goto(PLAYWRIGHT_START_URL)
        input("Please log in manually. Once you're done, press Enter here to save your session. ")
        context.storage_state(path=SESSION_FILE)
        print(f"Session saved.")
        browser.close()


def upload_image_to_template(page: Page, image_path: str, nth: int = None, replace: bool = True) -> None:
    """
    Uploads an image to the selected slide/template editor on usebutter.com.
    Assumes you're already on the generator page and the Image block is selected.
    """
    assert os.path.isfile(image_path), f"Image file does not exist: {image_path}"

    def click_button_by_role(name: str):
        btn = page.get_by_role("button", name=name)
        if nth is None:
            btn.click()
        elif nth == 1:
            btn.first.click()
        else:
            btn.nth(nth - 1).click()

    try:
        if not replace:
            raise RuntimeError("Skipping Replace button due to is_empty=True")
        click_button_by_role("Remove Replace")
    except Exception:
        click_button_by_role("Click to upload or drag and")

    # Upload the file
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Upload Drop your files or").click()
    fc_info.value.set_files(image_path)

    # Select uploaded image
    try:
        page.locator("#simple-tabpanel-0 img").click()
    except Exception:
        page.get_by_role("img").nth(1).click()

    # Confirm the update
    page.get_by_role("button", name="(1) Update").click()


def fill_butter_template(template_data: dict[str, str]) -> None:
    ensure_browsers_installed()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=SESSION_FILE, accept_downloads=True)
        page = context.new_page()
        page.goto("https://www.usebutter.com/spotify-wrapped-2024-generator")
        page.wait_for_load_state("load")

        # Remove the existing slides
        page.get_by_role("button", name="Remove 2").get_by_label("Remove").click()
        page.get_by_role("button", name="Remove 2").get_by_label("Remove").click()
        page.get_by_role("button", name="Remove 1").click()

        # Create a new intro
        page.get_by_role("button", name="Add Scene").click()
        page.locator("div").filter(has_text=re.compile(r"^IntroRectanglesDiamondsRibbons$")).get_by_role("img").nth(1).click()
        page.locator("div").filter(has_text=re.compile(r"^Subtitle$")).first.click()
        page.get_by_role("button", name="Add Scene").click()
        page.get_by_role("paragraph").filter(has_text="You ‘[BLANK]’ 32 times this").click()
        page.get_by_role("textbox").filter(has_text="You ‘[BLANK]’ 32 times this").fill("Your May\nSpotify Unwrapped\nis Here")
        page.get_by_role("textbox").nth(2).fill("23")
        page.get_by_text("Wrapped Rectangles").click()
        page.get_by_role("paragraph").filter(has_text="You’re in the top 1% of [BLANK]").click()
        page.get_by_role("textbox").filter(has_text="You’re in the top 1% of [BLANK]").fill("Make Yours at https://github.com/Meleagrista/py-spotify-unwrapped")
        page.get_by_role("textbox").nth(2).fill("7")
        page.get_by_text("Wrapped Rectangles").click()

        # Add scenes
        page.get_by_role("button", name="Add Scene").click()
        page.locator("div").filter(has_text=re.compile(r"^IntroRectanglesDiamondsRibbons$")).get_by_role("img").nth(2).click()
        page.locator("div:nth-child(5) > img").click()
        page.get_by_role("button", name="Add Scene").click()
        page.wait_for_load_state("load")

        # Change subtitle...
        page.get_by_text("No one asked for this.").click()
        page.get_by_role("textbox").filter(has_text="No one asked for this.").fill("Your #1 artist this month")

        # ...and change the position of the subtitle
        page.get_by_text("Position").click()
        page.locator("input[type=\"text\"]").nth(3).fill("100")
        page.get_by_text("Wrapped Diamond").click()

        # Change the title
        page.get_by_text("Your [BLANK] Era").click()
        page.get_by_role("textbox").filter(has_text="Your [BLANK] Era").fill(template_data.get('artist_01'))
        page.get_by_role("textbox").nth(2).fill("20")
        page.get_by_text("Wrapped Diamond").click()

        # Change the image
        page.locator("#componentSelector div").filter(has_text="Image").click()
        upload_image_to_template(page, template_data.get('artist_image_01'))
        page.get_by_text("Wrapped Diamond").click()

        # Change the background
        page.locator("#sceneEditCards").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
        page.locator("#rc-editable-input-1").fill("#EB4034")
        page.get_by_role("button").click()
        page.locator("#sceneEditCards").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
        page.locator("#rc-editable-input-2").fill("#FF5CF1")
        page.get_by_role("button").click()

        # Add more scenes
        page.get_by_role("button", name="Add Scene").click()
        page.locator("div:nth-child(6) > img").click()
        page.locator("div").filter(has_text=re.compile(r"^IntroRectanglesDiamondsRibbons$")).get_by_role("img").nth(3).click()
        page.get_by_role("button", name="Add Scene").click()
        page.wait_for_load_state("load")

        # Change the background
        page.locator("#sceneEditCards").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(1).click()
        page.locator("#rc-editable-input-3").fill("#EB4034")
        page.get_by_role("button").click()
        page.locator("#sceneEditCards").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
        page.locator("#rc-editable-input-4").fill("#FF5CF1")
        page.get_by_role("button").click()
        page.locator("#sceneEditCards").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
        page.locator("#rc-editable-input-5").fill("#EB4034")
        page.get_by_role("button").click()
        page.locator("#sceneEditCards").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
        page.locator("#rc-editable-input-6").fill("#FF5CF1")
        page.get_by_role("button").click()
        page.get_by_role("textbox").fill("50")
        page.get_by_role("checkbox").uncheck()

        # Change the title
        page.get_by_text("Your Top [BLANK]").click()
        page.get_by_role("textbox").filter(has_text="Your Top [BLANK]").fill("Your Top Songs")
        page.locator("div:nth-child(3) > div > div > div > div > .MuiBox-root > .css-129-container-ref").click()
        page.locator("input[type=\"text\"]").nth(3).fill("-127.5")
        page.get_by_text("Wrapped Ribbons").click()

        # Change the ranking
        page.locator("#componentSelector").get_by_text("Ranking").click()
        page.locator("div:nth-child(2) > .MuiBox-root > svg").click()
        page.locator("div:nth-child(2) > .MuiBox-root > svg").click()
        page.locator(".MuiBox-root > .MuiInputBase-root > .MuiInputBase-input").first.fill("40")
        page.locator("div:nth-child(4) > div > div > div > div > .MuiBox-root > .css-129-container-ref").click()
        page.locator("div").filter(has_text=re.compile(r"^xy$")).get_by_role("textbox").nth(1).fill("24")

        # Add tracks
        page.get_by_role("textbox", name="Title", exact=True).first.fill(template_data.get('track_01'))
        page.get_by_role("textbox", name="Subtitle").first.fill(template_data.get('track_artist_01'))
        upload_image_to_template(page, template_data.get('track_image_01'), 1)

        # ---

        page.get_by_role("textbox", name="Title", exact=True).nth(1).fill(template_data.get('track_02'))
        page.get_by_role("textbox", name="Subtitle").nth(1).fill(template_data.get('track_artist_02'))
        upload_image_to_template(page, template_data.get('track_image_02'), 2)

        # ---

        page.get_by_role("textbox", name="Title", exact=True).nth(2).fill(template_data.get('track_03'))
        page.get_by_role("textbox", name="Subtitle").nth(2).fill(template_data.get('track_artist_03'))
        upload_image_to_template(page, template_data.get('track_image_03'), 3)

        # ---

        page.get_by_role("textbox", name="Title", exact=True).nth(3).fill(template_data.get('track_04'))
        page.get_by_role("textbox", name="Subtitle").nth(3).fill(template_data.get('track_artist_04'))
        upload_image_to_template(page, template_data.get('track_image_04'), 1, False)

        # ---

        page.get_by_role("textbox", name="Title", exact=True).nth(4).fill(template_data.get('track_05'))
        page.get_by_role("textbox", name="Subtitle").nth(4).fill(template_data.get('track_artist_05'))
        upload_image_to_template(page, template_data.get('track_image_05'), 1, False)


        # Export the video
        page.get_by_text("Wrapped Ribbons").click()
        page.get_by_role("button", name="Remove 1").get_by_label("Remove").click()
        page.get_by_role("button", name="Export Video").click()

        print("Starting download, this may take a while...")
        with page.expect_download(timeout=900_000) as download_info:
            page.locator("div").filter(has_text=re.compile(r"^Download nowFaster exportfor newer computers$")).first.click()
        download = download_info.value

        # Save download to provided path
        download_path = DOWNLOAD_DIR / f"spotify-unwrapped-{template_data.get('month').lower()}.mp4"
        download_path.parent.mkdir(parents=True, exist_ok=True)
        download.save_as(str(download_path))

        # Clean up
        page.get_by_text("Close").click()
        context.close()
        browser.close()

if __name__ == "__main__":
    generate_login_session()