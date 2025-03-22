class Config:


    instruction="""
    <style>
    #_otree-title{
        margin:0;
        padding:0;
    }

    .otree-body{
        margin:0;
        padding:0;
    }
    .container{
        padding: 0;
        margin: 0;
    }
    .card-body{
        padding: 0;
    }
    </style>    
    <div class="card p-4 mx-auto  shadow  border-0  align-middle h-50 rounded-4" style="max-width: 400px;">
        <div class="card-body lh-lg  ">
            <ol>
                <li>Click the "Roll Dice" button</li>
                <li>Input the result in the text field</li>
                <li>Wait for the other players to input</li>
                <li>Go to the next round or Exit</li>
            </ol>
        </div>
        <div class="d-grid col-6 mx-auto">
            <button class="otree-btn-next btn btn-primary">Next</button>
        </div>
    </div>
"""

    dice="""
        <div class="col-12 h-25 d-flex shadow light-blue rounded-4 pb-3 align-items-center  justify-content-center" id="dice">
            <div id='dice1' class="dice dice-one">
                <div id="dice-one-side-one" class='side one'>
                    <div class="dot one-1"></div>
                </div>
                <div id="dice-one-side-two" class='side two'>
                    <div class="dot two-1"></div>
                    <div class="dot two-2"></div>
                </div>
                <div id="dice-one-side-three" class='side three'>
                    <div class="dot three-1"></div>
                    <div class="dot three-2"></div>
                    <div class="dot three-3"></div>
                </div>
                <div id="dice-one-side-four" class='side four'>
                    <div class="dot four-1"></div>
                    <div class="dot four-2"></div>
                    <div class="dot four-3"></div>
                    <div class="dot four-4"></div>
                </div>
                <div id="dice-one-side-five" class='side five'>
                    <div class="dot five-1"></div>
                    <div class="dot five-2"></div>
                    <div class="dot five-3"></div>
                    <div class="dot five-4"></div>
                    <div class="dot five-5"></div>
                </div>
                <div id="dice-one-side-six" class='side six'>
                    <div class="dot six-1"></div>
                    <div class="dot six-2"></div>
                    <div class="dot six-3"></div>
                    <div class="dot six-4"></div>
                    <div class="dot six-5"></div>
                    <div class="dot six-6"></div>
                </div>
            </div>
        </div>

"""

    script="""
    <script>



      function verify() {
        document.getElementById("submit").disabled = false;
      }

      function rollDice() {
        verify()
        var elDiceOne       = document.getElementById('dice1');
        var elComeOut       = document.getElementById('roll');  
        var inputReal       = document.getElementById('realvalue')

        var diceOne   =     Math.floor((Math.random() * 6)+ 1);

        // correcter values since the cidde show are not correct
        var listOfVal = [1, 5, 6, 3, 4, 2];

        // inputReal.value = listOfVal[diceOne-1];

        console.log(diceOne + " real");
        console.log(listOfVal[diceOne-1] + ' howw?');

        for (var i = 1; i <= 6; i++) {
            elDiceOne.classList.remove('show-' + i);
            if (diceOne === i) {
                elDiceOne.classList.add('show-' + i);   
                }
            }   
        }


    </script>


"""

    button="Roll Dice!"