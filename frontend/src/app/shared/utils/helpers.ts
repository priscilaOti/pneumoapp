export const isMobile: boolean = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

export const scrollTo = (top: number = 2500) => window.scroll({
    top,
    left: 0,
    behavior: 'smooth'
});