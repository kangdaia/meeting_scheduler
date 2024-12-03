/** @type {import('tailwindcss').Config} */
import { radixThemePreset } from 'radix-themes-tw';
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  presets: [radixThemePreset],
  plugins: [
    "postcss-import": {},
  ],
}