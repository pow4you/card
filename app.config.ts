

export default defineAppConfig({
    navigation: [
        {path: "/", title: "Home", icon: "ph:house-light", active_icon: "ph:house-bold"},
        {path: "/#Pronouns", title: "Pronouns", icon: "ph:sparkle-light", active_icon: "ph:sparkle-bold"},
        {path: "/#Socials", title: "Socials", icon: "ph:smiley-wink-light", active_icon: "ph:smiley-wink-bold"},
        {path: "/about", title: "About", icon: "ph:book-open-text-light", active_icon: "ph:book-open-text-bold"},
    ],
    socials : [
        {
            shortName: "github", longName: "Github", userName:"pow4you", url: "https://github.com/pow4you", 
            profilePic: "https://avatars.githubusercontent.com/u/129770852",
            description:"Pow4you on Github. There you can find whatever I'm currently working on, what I'm learning and what I'm trying to learn.",
            icon:"ph:github-logo-bold"
        },
        
        {
            shortName: "discord",
            longName: "Discord",
            userName: "powowocat",
            url: "https://discord.com/users/powowocat",
            profilePic: "https://cdn.discordapp.com/avatars/327795737771376640/878464b244022570b0ac1df0983d356a?size=1024",
            description: "Connect with me on Discord.",
            icon: "ph:discord-logo"
        },
        {
            shortName: "instagram",
            longName: "Cosplay Instagram",
            userName: "powcosplay",
            url: "https://instagram.com/powcosplay",
            description: "Follow my cosplay journey on Instagram.",
            icon: "ph:instagram-logo-thin"
        },
        {
            shortName: "instagram",
            longName: "Personal Instagram",
            userName: "powowocat",
            url: "https://instagram.com/powowocat",
            description: "Check out my personal Instagram profile.",
            icon: "ph:instagram-logo-thin"
        },
        {
            shortName: "twitter",
            longName: "Twitter",
            userName: "PowowoCat",
            url: "https://twitter.com/PowowoCat",
            description: "Follow me on Twitter for updates and tweets.",
            icon: "ph:twitter-logo-thin"
        },
        {
            shortName: "bsky",
            longName: "BlueSky",
            userName: "pow.bsky.social",
            url: "https://bsky.app/profile/pow.bsky.social",
            description: "Find me on Bsky for more updates.",
            icon: "ph:cloud-sun-thin"
        }
        //tumblr
        //steam
        //youtube
    ],
    ger_host: false
})