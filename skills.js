function solution(skills) {
     n = skills.length;
     team_remaining = [...Array(n).keys()];
     last_mile = new Array(n).fill(-1);
     count_laps = 1;

    while (team_remaining.length > 1) {
        let new_players = [];
        for (let i = 0; i < team_remaining.length; i += 2) {
            let team_1 = team_remaining[i];
            let team_2 = (i + 1 < team_remaining.length) ? team_remaining[i + 1] : null;
            let winners_tag;
            if (team_2 === null || skills[team_1] > skills[team_2]) {
                winners_tag = team_1;
            } else {
                winners_tag = team_2;
            }
            new_players.push(winners_tag);
            last_mile[team_1] = count_laps;
            if (team_2 !== null) {
                last_mile[team_2] = count_laps;
            }
        }
        team_remaining = new_players;
        count_laps++;
        // console.log("Lap:", count_laps, "Remaining Players:", team_remaining);
        // console.log("Final Lap:", last_mile);
    }
    return last_mile;
} 
    //return solution(skills)

// function solution(skills) {
//     return solution(skills);
// }

const skills = [3, 4, 2, 1];
console.log("Skills:", skills);
console.log("Final Laps:", solution(skills));
