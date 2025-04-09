from string import Template

class Config:
    def __init__(self, header, steps, button, round, dice, script):
        self.instruction = self.get_Instruction( header, steps)
        self.button = button
        self.round = round 
        self.dice = dice
        self.script = """

<script>
    function verify() {
        document.getElementById("submit").disabled = false;
    }

    function rollDice() {
        verify();
        var elDiceOne       = document.getElementById('dice1');
        var elComeOut       = document.getElementById('roll');  
        var inputReal       = document.getElementById('id_dice');

        var diceOne   =     Math.floor((Math.random() * 6)+ 1);

        // correcter values since the cidde show are not correct
        var listOfVal = [1, 5, 6, 3, 4, 2];

        inputReal.value = listOfVal[diceOne-1];

        console.log(diceOne + " real");
        console.log(inputReal.value + ' howw?');

        for (var i = 1; i <= 6; i++) {
            elDiceOne.classList.remove('show-' + i);
            if (diceOne === i) {
                elDiceOne.classList.add('show-' + i);   
            }
        }   
    }

</script>   
"""

    def get_Instruction(self, header, steps) : 
        return f"""
        <div class="card-body lh-lg  ">
            <p> {header}</p>
            <ol>
                {"".join([f"<li>{step}</li>" for step in steps])}
            </ol>
        </div>
"""
    
    def format_string(self):
        print(self.instruction)
        template = Template(self.instruction)
        self.instruction  = template.substitute(button=self.button, round=self.round)
