const puppeteer = require('/home/kingb/aim-browser/node_modules/puppeteer-core');

(async () => {
  try {
    const browser = await puppeteer.connect({
      browserURL: 'http://127.0.0.1:9222'
    });
    const pages = await browser.pages();
    const page = pages[0];
    console.log("Navigating to sannysoft...");
    await page.goto('https://bot.sannysoft.com/', { waitUntil: 'networkidle2' });
    console.log("Navigation complete. User should be able to see the results.");
    browser.disconnect();
  } catch (err) {
    console.error("Error:", err);
  }
})();
