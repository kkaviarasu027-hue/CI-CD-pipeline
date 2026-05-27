const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: false,
        slowMo: 500,
        channel: 'chrome'
    });

    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        await page.goto('https://peaceful-florentine-1dbd10.netlify.app/', {
            waitUntil: 'domcontentloaded'
        });

        await page.waitForSelector('input', { timeout: 5000 }).catch(() => {});

        // 1. Fill Username/Mail ID
        const emailInput = page.getByPlaceholder('college.admin@jozuna.com');
        await emailInput.fill('kalpana@yopmail.com');

        // 2. Fill Password
        const passwordInput = page.getByPlaceholder('Enter password');
        await passwordInput.fill('Kal@2026');

        // 3. Click the "Stay logged in on this device" checkbox text
        // Playwright will find the text label and click it, which automatically toggles the box
        await page.click('text=Stay logged in on this device');

        // 4. Click the Login button
        await page.click('button:has-text("Login")');

        await page.waitForLoadState('networkidle');
        // Wait for 3000 milliseconds (3 seconds)


        console.log('✅ Login successful!');
        await page.waitForTimeout(5000);
    } catch (error) {
        console.log('❌ Login failed:', error);
    } finally {
        await browser.close();
    }
})();