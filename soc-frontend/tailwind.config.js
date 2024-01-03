module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js"
  ],
  darkMode: 'class',
  
  theme: {
    extend: {
      backgroundColor:{
        'dark': '#333',
      },
      textColor:{
        'dark': '#fff',
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
]
}