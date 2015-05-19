function play_audio(){
    document.getElementById('audio').play()
}

function randomWord() {

    var selection = Object.keys(words);
    var word = selection[Math.floor(Math.random()*selection.length)];
    var file_name = words[word];
    var file_parts = file_name.split("_");
    var file_src = 'static/mp3/'+file_parts[0]+'/'+file_name+'.mp3';
    $("#word").text(word);
    $("#audio").attr('src', file_src);

}

$(function(){

    randomWord();
    $("#next_word").on("click", randomWord);
    $("#play_audio").on("click", play_audio);

});