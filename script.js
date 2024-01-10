/*short for 'context'*/
const ctx = document.getElementById("myChart");

const gameTitles = ["Barrage",
    "Barrage",
    "Barrage",
    "Tigris and Euphrates",
    "Brass",
    "Transcontinental",
    "Food Chain Magnate",
    "Food Chain Magnate",
    "Food Chain Magnate \n(New Milestones)",
    "Winter Kingdom",
    "Pax Pamir",
    "High Frontier 4 All",
    "High Frontier 4 All"
];

const totalAverageRating = [43.86 * 2,
    43 * 2,
    44.07 * 2,
    41.23 * 2,
    48.4 * 2,
    32.8 * 2,
    39.43 * 2,
    38.98 * 2,
    42.63 * 2,
    29.85 * 2,
    37 * 2,
    43.6 * 2,
    45.67 * 2
];

const dateOfPlayNotFormatted = [new Date("2022-12-17").toUTCString(),
    new Date("2023-01-07").toUTCString(),
    new Date("2023-01-14").toUTCString(),
    new Date("2023-01-21").toUTCString(),
    new Date("2023-01-28").toUTCString(),
    new Date("2023-02-11").toUTCString(),
    new Date("2023-03-04").toUTCString(),
    new Date("2023-03-11").toUTCString(),
    new Date("2023-03-25").toUTCString(),
    new Date("2023-04-13").toUTCString(),
    new Date("2023-05-10").toUTCString(),
    new Date("2023-05-18").toUTCString(),
    new Date("2023-06-03").toUTCString()
];

const dateOfPlay = [];

const titleDate = [];

for (let i = 0; i < dateOfPlayNotFormatted.length; i++) {
    const dateString = dateOfPlayNotFormatted[i].toString();
    dateOfPlay.push(dateString.slice(5, 16));
}

for (let i = 0; i < dateOfPlay.length; i++) {
    titleDate.push([gameTitles[i], dateOfPlay[i]])
}


const labelChart = 'Total Group Score - out of 100'

const titleToolTip = (tooltipItems) => {
    return '';
}

/*instantiate a new chart*/
var allGamesChart = new Chart(ctx, {
    type: "bar",
    data: {
        datasets: [
            {
                label: labelChart,
                data: totalAverageRating,
                backgroundColor: 'rgba(0, 225, 255, 0.8)'
            }
        ],
    },
    options: {
        scales: {
            x: {
                labels: titleDate,
                grid: {
                    display: false
                }
            },
            y: {
                suggestedMax: 100,
                grid: {
                    display: false
                }
            }
        },
        plugins: {
            tooltip: {
                yAlign: 'bottom',
                displayColors: false,
                callbacks: {
                    title: titleToolTip,
                    label: function (tooltipItem) {
                        let tooltipText = '';
                        if (tooltipItem.dataset.data[tooltipItem.dataIndex] != null)
                            tooltipText = tooltipItem.dataset.data[tooltipItem.dataIndex].toString();
                        return tooltipText
                    },
                    titleMarginBottom: 0
                }
            },
            annotation: {
                annotations: {
                    minCutoff: {
                        type: 'line',
                        yMin: 70,
                        yMax: 70,
                        borderColor: 'rgba(255, 0, 0, 1)',
                        borderWidth: 2
                    }
                }
            }
        },
        "horizontalLine": [{
            "y": 70,
            "style": "rgba(255, 0, 0, .8)",
            "text": "max"
        }],
        maintainAspectRatio: false
    }
})
