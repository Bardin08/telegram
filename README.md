<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://telegram.org">Telegram</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
    <a href="https://github.com/catppuccin/telegram/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/telegram?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/telegram/issues"><img src="https://img.shields.io/github/issues/catppuccin/telegram?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/telegram/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/telegram?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
  <img src="assets/res.webp"/>
</p>

## Previews

<details>
<summary>🖥 Desktop</summary>
<details>
<summary>🌻 Latte</summary>
<img src="assets/desktop/latte.webp"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="assets/desktop/frappe.webp"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="assets/desktop/macchiato.webp"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="assets/desktop/mocha.webp"/>
</details>
</details>

<details>
<summary>📱 Mobile</summary>
<details>
<summary>🌻 Latte</summary>
<img src="assets/mobile/latte.webp"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="assets/mobile/frappe.webp"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="assets/mobile/macchiato.webp"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="assets/mobile/mocha.webp"/>
</details>
</details>

## Usage

* [🌻 Latte Crema](https://t.me/addtheme/ctp_latte_crema)
* [🪴 Frappé Crema](https://t.me/addtheme/ctp_frappe_crema)
* [🌺 Macchiato Crema](https://t.me/addtheme/ctp_macchiato_crema)
* [🌿 Mocha Crema](https://t.me/addtheme/ctp_mocha_crema)

Open the link in Telegram for iOS, Android or desktop and apply the theme. Each link carries a separate file per app.

To import a file instead, take it from `src/<flavor>/`:

| App | File | How |
|---|---|---|
| iOS | `catppuccin-<flavor>-crema.tgios-theme` | Send it to Saved Messages, tap it and apply. If the old chat pattern stays, reset the chat background to the theme default. |
| Android | `catppuccin-<flavor>-crema.attheme` | Send it to Saved Messages, tap it and apply. |
| Desktop | `catppuccin-<flavor>-crema.tdesktop-palette` | Settings → Chat Settings → right-click a theme → Edit → Import existing theme. |
| macOS (App Store) | `catppuccin-<flavor>-crema.palette` | Finder cannot open it. Open Settings, click the Settings tab icon five times quickly, choose Import Palette and pick the file. |

## 🐱 Development (for the desktop version)

- The desktop version uses Go to build files for all flavours. To build a flavour, run `go run main.go --color <flavour-name>`. This creates a desktop theme file inside `src/<flavour-name>/<flavour-name>_desktop`. Use `--accent` flag to change accent color: `--accent ctpRed`; `ctpGreen` - default.
- You are supposed to change the colours inside the `build/template.go.tpl` file. 
- Rebuild flavours after editing the template file. 

## 💝 Thanks to

- [Andreas Grafen](https://github.com/andreasgrafen)
- [ghostx31](https://github.com/ghostx31)
- [Name](https://github.com/NamesCode)
- [jasoncrevier](https://github.com/jasoncrevier)

&nbsp;

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center">Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
<p align="center"><a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
