/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                background: "#0a0c10",
                surface: "#11141a",
                primary: "#3b82f6",
                secondary: "#6366f1",
                accent: "#8b5cf6",
                text: {
                    primary: "#f8fafc",
                    secondary: "#94a3b8",
                    muted: "#64748b",
                },
            },
            backgroundImage: {
                'glass-gradient': 'linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01))',
            },
            boxShadow: {
                'glass': '0 8px 32px 0 rgba(0, 0, 0, 0.37)',
            },
        },
    },
    plugins: [],
}
