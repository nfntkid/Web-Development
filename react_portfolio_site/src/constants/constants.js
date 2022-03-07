/*create a list of dictionaries that hold the information 
for the projects that you've done. Export them to use in the 
timeline and projects components 
*/
export const projects = [
  {
    title: "Full Stack image repository",
    description: "",
    image: "/images/CRUD_APP.png",
    tags: ["bootstrap", "flask", "jinja", "sql-lite"],
    source:
      "https://github.com/nfntkid/web-dev/tree/main/shopify_intern_challenge",
    visit: "https://google.com",
    id: 0,
  },
  {
    title: "Ethereum Price Analysis",
    description: "",
    image: "/images/PLOT_CHART.png",
    tags: ["matplotlib", "pandas_datareader", "mplfinance"],
    source:
      "https://github.com/nfntkid/Data-Science/tree/main/ethereum_price_analysis",
    visit: "https://google.com",
    id: 0,
  },
  {
    title: "Startup Analysis",
    description: "",
    image: "/images/startup_output.png",
    tags: ["jupyter notebook", "pandas"],
    source:
      "https://github.com/nfntkid/Data-Science/tree/main/startup_analysis",
    visit: "https://google.com",
    id: 0,
  },
];

// Create the information for the timeline carousel
export const TimeLineData = [
  { year: 2014, text: "Discovered programming through music production" },
  {
    year: 2017,
    text: "Interned at digital marketing company 'MyAdvice' (formerly AdviceMedia)",
  },
  { year: 2018, text: "Began teaching at The Coder School Syosset" },
  { year: 2019, text: "Launched the website for my music label 'nfntny.com'" },
  { year: 2021, text: "Started my full stack journey" },
];

export const data = [{ number: 200, text: "Students" }];
