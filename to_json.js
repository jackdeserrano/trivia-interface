// taggagii

const fs = require('fs');

const text = fs.readFileSync('__trivia.txt', 'utf-8');

const split_text = text.split('\n\n');

const output = {};

for (let i = 0; i < split_text.length; ++i) {
    const question_data = split_text[i].split('\n');
    const [question, answer, index] = question_data;
    output[index] = {
        question,
        answer,
        index,
    };
}

fs.writeFileSync('__trivia.json', JSON.stringify(output, null, 2));
