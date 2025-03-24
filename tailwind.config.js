module.exports = {
    content: [
      "./templates/**/*.{html,js}",
      "./static/**/*.{css,js}",
    ],
    theme: {
      extend: {},
    },
    plugins: [require("daisyui")],
    daisyui: {
      themes: [
        "light",
        "dark",
        "cupcake",
        {
          customtheme: {
            primary: "#570DF8",
            secondary: "#F000B8",
            accent: "#37CDBE",
            neutral: "#3D4451",
            "base-100": "#FFFFFF",
            info: "#3ABFF8",
            success: "#36D399",
            warning: "#FBBD23",
            error: "#F87272",
          },
        },
      ],
    },
  };