let showCardInfo = (event) => {
    let infoBlock = event.target.nextSibling.parentElement.getElementsByTagName('div')[0];
    infoBlock.className = 'movie-card-text-active';
}

let closeCardInfo = (event) => {
    let infoBlock = event.target.getElementsByTagName('div')[0];
    infoBlock.className = 'movie-card-text-nonactive';
}