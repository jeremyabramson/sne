const scrapedin = require('scrapedin')
const readline = require('readline')
const fs = require('fs')

const scrapeFunc = async (urllist) => {
	const profileScraper = await scrapedin({ email: EMAIL, password: PASSWORD, /*isHeadless: false*/ }) // change this
	for(let url of urllist) {
		let filePath = url.substring(28) // take everything after the initial linkedin url
		filePath = filePath.replace("/", "")
		if (!fs.existsSync('C:\\Users\\ryanw\\Desktop\\linkedins\\' + filePath + '.txt')) { // check if file is already created, so you don't repeat work if you stop/rerun the script
			console.log(url)
			const profile = await profileScraper(url)
			if(JSON.stringify(profile) !== '{}') {
				writeToFile(JSON.stringify(profile), filePath)
			}
		}

	}
	console.log("Finished scraping!")
}

const writeToFile = (s, filename) => {
	fs.writeFile('C:\\Users\\ryanw\\Desktop\\linkedins\\' + filename + '.txt', s, (err) => {
		if (err) throw err;
		console.log('saved');
	});
}

const main = () => {

	const readInterface = readline.createInterface({
	    input: fs.createReadStream('C:\\Users\\ryanw\\Desktop\\ng_linkedins_large_v2_clean_v2.txt'),
	    output: process.stdout,
	    console: false,
	    terminal: false,
	});

	linkedins = []
	readInterface.on('line', (line) => {
		if(line.length !== 0)
			linkedins.push(line)
	})
	scrapeFunc(linkedins)
}

main()