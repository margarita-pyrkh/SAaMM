let numbers = [];
const barsInChart = 20
let myChart;

function generateNumbers(a, r, m, numbersAmount) {
	for (let i = 0; i < numbersAmount; i += 1) {
		const rNew = (a * r) % m;
		const x = rNew / m;
		r = rNew;
		numbers.push(x);
	}
}

function findExpectation() {
	const sum = numbers.reduce((a, b) => a + b, 0);
	return sum / numbers.length;
}

function findDispersion(m) {
	const sum = numbers.reduce((a, b) => a + (b - m)*(b - m), 0);
	return sum / numbers.length;
}

function findPeriod() {
	const compareValue = numbers[numbers.length - 1];
	const lastIndex = numbers.length - 1;
	const firstIndex = numbers.indexOf(compareValue);
	const secondIndex = numbers.indexOf(compareValue, firstIndex + 1);
	const period = secondIndex - firstIndex; 
	return period;
}

function findAperiodicLength() {
	
}

function initializeChart() {
	if (myChart) {
		myChart.destroy();
	}

	const minValue = Math.min(...numbers);
	const maxValue = Math.max(...numbers);
	
	const range = maxValue - minValue;
	const barLength = range / barsInChart;

	const boundaries = [];

	for (let i = 0; i < barsInChart; i += 1) {
		if (i === 0) {
			boundaries.push({
				min: minValue,
				max: minValue + barLength,
			});
		} else {
			boundaries.push({
				min: boundaries[i - 1].max,
				max: boundaries[i - 1].max + barLength,
			});
		}
	}

	const frequencies = boundaries.map((boundary) => {
		let numberOfHits = 0;
		numbers.forEach((number) => {
			if (number >= boundary.min && number < boundary.max) {
				numberOfHits += 1;
			}
		});
		return numberOfHits / numbers.length;
	});

	const ctx = document.getElementById("chart");
	myChart = new Chart(ctx, {
		type: 'bar',
		data: {
		    labels: frequencies.map((frequency, index) => index + 1),
		    datasets: [{
		        data: frequencies,
		        backgroundColor: '#a6c4f4',
		    }]
		},
		options: {
			legend: {
				display: false,
			},
			scales: {
				xAxes: [{
					display: true,
					ticks: {
						autoSkip: true,
					},
				}],
			},
		}
	});
}

function showResults(m, d, p) {
	const cardResults = document.getElementById("card__results");
	cardResults.style.display = 'block';
	
	const expectation = document.getElementById("expectation");
	expectation.innerText += m;
}

function onFormSubmit(event) {
	event.preventDefault();
	const a = parseInt(document.valuesForm.aValue.value);
	const r = parseInt(document.valuesForm.rValue.value);
	const m = parseInt(document.valuesForm.mValue.value);
	const numbersAmount = parseInt(document.valuesForm.numbersAmount.value);

	numbers = [];
	
	generateNumbers(a, r, m, numbersAmount);

	console.log(numbers);

	const expectation = findExpectation();
	const dispersion = findDispersion(expectation);	
	const period = findPeriod();

	initializeChart();
	
	showResults(expectation, dispersion, period);
}