import links from "~/conf/links";
import pronouns from "~/conf/pronouns";

export default defineAppConfig({
    navigation: [
        {path: "/", title: "Home", icon: "ph:house-light", active_icon: "ph:house-bold"},
        {path: "/#Pronouns", title: "Pronouns", icon: "ph:sparkle-light", active_icon: "ph:sparkle-bold"},
        {path: "/#Socials", title: "Socials", icon: "ph:heart-light", active_icon: "ph:heart-bold"},
        {path: "/about/", title: "About", icon: "ph:book-open-text-light", active_icon: "ph:book-open-text-bold"},
        {path: "https://gofund.me/863ebe94", title: "FFS Fund", icon: "uil:medical", active_icon: "uil:medical"},
    ],
    
    pronouns : pronouns,
    links : links,

    ger_host: false
})