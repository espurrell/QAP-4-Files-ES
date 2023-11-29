// QAP 4 - JavaScript
//Prepared for: Peter Rawthorne
//Prepared by: Ed Spurrell
//Completed: November 23 2023
// add github here

const customer = {
    firstName: 'susan',
    lastName: 'spurrell',
    birthday: '18',
    birthmonth: 'July',
    birthyear: '1988',
    gender: 'non-binary',
    roompreference: ['single', 'double', 'queen', 'honeymoon'],
    paymentmethod: AMEX,
    address: {
        street: '171 Craigmillar Ave',
        city: 'St. Johns',
        province: 'NL',
        postcode: 'A1E2A2',
        country: 'Canada'
    },
    phoneNumb: '7097699196',
    checkin: '13-11-2023',
    checkoutdate: {
        day: '20',
        month: '11',
        year: '2023',
    }
}

var formattedCheckOut = custStay.dates.checkOutDate[0].toLocaleDateString('en-CA');

//determine age

function calculateAge(birthdate) {
    const today = new Date();
    const birthDate = new Date(birthdate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    
        return age;
    
    }

//Duration Calculation
this .calculateDurationOfStay = function () {
    const millisecondsInADay = 24 * 60 * 60 * 1000;
    const checkInTime = this.checkInDate.getTime();
    const checkOutTime = this.checkOutDate.getTime();
    const durationInMilliseconds = checkOutTime - checkInTime;
    
    return Math.ceil(durationInMilliseconds / millisecondsInADay);
    }


    // template literal string - properly formatted html that describes the customer

let val;
val = `Hello, my name is ${firstName} ${lastName}. I identify as ${gender} and I am ${age} years of age. When vacationing with my friends I prefer to book ${roompreference}. For this upcoming trip I will be staying from ${checkin} to ${formattedCheckOut}. My Contact information is as follows:${phoneNumb} for my direct line, my address: ${address.street} ${address.city} ${address.province} ${address.postcode} and I intend to pay via ${paymentmethod}.`


console.log(val);


