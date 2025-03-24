class Config:

    def __init__(self, cost, probability, endowment):
        self.instruction = self.get_Instruction(cost, probability, endowment)

    def get_Instruction(self, cost, probability, endowment) : 
        return f"""
        <div class="card-body lh-lg  ">
            <ol>
                <li>Enter the design contribution with the limit of the Endowment: <strong>{endowment}</strong> </li>
                <li>There will be an incoming storm with a probability of <strong>{probability}</strong></li>
                <li>To make sure that you will survive the storm, you to have accumulated contribution of equal to the cost of the early warning system: <strong>{cost}</strong></li>
                <li>However, there is a chance that the strom will not come, so make sure that to think wisely!</li>
            </ol>
        </div>
"""