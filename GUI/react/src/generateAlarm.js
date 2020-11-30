var affectedSystemsArray = ["DNS-Server", "Database", "PAX-System", "IT-Desk", "Firewall", "Switchboard", "File-Server", "Backup-Server", "Print-Server", "Mail-Server", "Coffee Machine"];
var suspectedAttackTypeArray = ["SQL-Injection", "Denial of Service", "Man in the Middle", "Brute Force", "Virus", "Trojan", "Registry-Attack", "Remote Binary Planting", "Server Message Block"];
var automaticReactionArray = ["System-Shutdown", "Database-Shutdown", "System-Restart", "Disconnect from Internet", "Disconnect affected Systems", "Blocked User-Login"]
var checkListArray = ["restart the system", "call Incident-Response-Team", "reset login data", "stop all departures", "shut down the database", "stop all arrivals", "notify your manager", "drink some coffee", "take a break", "change server location", "get help"]

function shuffle(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

function generateRandomAlarm() {

    var randomProbability = Math.floor(Math.random() * 26) + 75

    return {
        id: Math.floor(Math.random() * 1000000),
        time: ( + new Date() ),
        affectedSystems: [shuffle(affectedSystemsArray).splice(affectedSystemsArray.length - (1 + Math.floor(Math.random() * 2)))],
        suspectedAttackType: suspectedAttackTypeArray[Math.floor(Math.random() * suspectedAttackTypeArray.length)],
        probability: randomProbability,
        automaticReaction: randomProbability > 95 ? [shuffle(automaticReactionArray).splice(automaticReactionArray.length - (1 + Math.floor(Math.random() * 1)))] : [],
        checklist: shuffle(checkListArray).splice(checkListArray.length - (2 + Math.floor(Math.random() * 5)))
    }
}

export { generateRandomAlarm };