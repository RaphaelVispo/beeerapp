class Config:

    def __init__(self, boat, threshold, fish):
        self.instruction = self.get_Instruction(boat, threshold, fish)

    def get_Instruction(self,boat, threshold, fish) : 
        return f"""
        <div class="card-body lh-lg  ">
            <p>Imagine you are a fisherman aiming to make a profit. The initial fish population is <strong>{fish}</strong>, but there's a catch: when the population reaches a certain threshold, it can double. Your goal is to maximize your catch while managing this dynamic resource.</p>
            <ol>
                <li>Decide how many fish to catch, keeping in mind the maximum limit of <strong>{boat}</strong> fish that your boat can hold.</li>
                <li>Be mindful of the <strong>{threshold}</strong>, which is the point where the fish population will double.</li>
                <li>Your objective is to survive and make the best decisions over 10 rounds. How long can you last while balancing the fish population and your catch?</li>
            </ol>
        </div>
"""