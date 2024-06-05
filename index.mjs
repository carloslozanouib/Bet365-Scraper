import { chromium } from 'playwright';

(async () => {
    const browser = await chromium.launch({ headless: false }); // Cambiar a true después de la depuración

    // Crear un contexto con un User-Agent personalizado
    const context = await browser.newContext({
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    });

    const page = await context.newPage();

    try {
        // Navegar directamente a la URL y esperar hasta que la página se cargue
        await page.goto('https://www.bet365.es/#/AC/B1/C1/D1002/E97746720/G40/H^1/', { waitUntil: 'networkidle', timeout: 60000 });

        // Comprobar si la página se ha redirigido al home
        if (page.url() !== 'https://www.bet365.es/#/AC/B1/C1/D1002/E97746720/G40/H^1/') {
            throw new Error('La página se redirigió al home. No se pudo cargar correctamente.');
        }

        // Esperar a que un contenedor conocido esté presente, indicando que la página ha cargado completamente
        await page.waitForSelector('.gl-MarketGroupContainer', { timeout: 60000 });

        // Capturar una captura de pantalla para depuración
        await page.screenshot({ path: 'screenshot.png', fullPage: true });

        const Matches_Euro_24 = await page.$$eval('.gl-MarketGroupContainer', (results) => {
            return results.map((the) => {
                const TeamNameElement = the.querySelector('.rcl-ParticipantFixtureDetailsTeam_TeamName');
                const TeamName = TeamNameElement ? TeamNameElement.innerText : 'Not Found';
                return { TeamName };
            });
        });

        console.log(Matches_Euro_24);
    } catch (error) {
        console.error('Error al extraer los datos:', error);
    } finally {
        await browser.close();
    }
})();
