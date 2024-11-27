import datetime
from typing import List, Dict
import matplotlib.pyplot as plt  # For visualizing campaign data

# Define the Campaign object
class Campaign:
    def __init__(self, name: str, start_date: datetime.date, stages: List[str]):
        """
        Initialize a new Campaign instance.
        :param name: Name of the campaign.
        :param start_date: Start date of the campaign.
        :param stages: List of stages for the campaign.
        """
        self.name = name
        self.start_date = start_date
        self.stages = stages
        self.current_stage = 0
        self.performance_metrics = {
            "emails_sent": 0,
            "open_rate": 0.0,
            "click_rate": 0.0,
        }

    def advance_stage(self):
        """Advance to the next stage of the campaign."""
        if self.current_stage < len(self.stages) - 1:
            self.current_stage += 1
            print(f"Campaign '{self.name}' advanced to stage: {self.stages[self.current_stage]}")
        else:
            print(f"Campaign '{self.name}' is complete!")

    def update_metrics(self, emails_sent: int, open_rate: float, click_rate: float):
        """
        Update campaign performance metrics.
        :param emails_sent: Number of emails sent in the campaign.
        :param open_rate: Open rate percentage (0-100).
        :param click_rate: Click rate percentage (0-100).
        """
        self.performance_metrics["emails_sent"] += emails_sent
        self.performance_metrics["open_rate"] = open_rate
        self.performance_metrics["click_rate"] = click_rate
        print(f"Updated metrics for '{self.name}': {self.performance_metrics}")

    def get_summary(self) -> Dict[str, any]:
        """Get a summary of the campaign."""
        return {
            "name": self.name,
            "start_date": self.start_date,
            "current_stage": self.stages[self.current_stage],
            "metrics": self.performance_metrics,
        }

    def visualize_performance(self):
        """Visualize the campaign performance metrics."""
        metrics = self.performance_metrics
        labels = ["Emails Sent", "Open Rate", "Click Rate"]
        values = [metrics["emails_sent"], metrics["open_rate"], metrics["click_rate"]]

        plt.bar(labels, values, color=["blue", "green", "orange"])
        plt.title(f"Performance Metrics for Campaign '{self.name}'")
        plt.ylabel("Values")
        plt.show()


# Example usage
if __name__ == "__main__":
    # Define campaign stages
    stages = ["Warning Shot", "Pre-Launch", "Launch", "Post-Launch"]

    # Create a campaign instance
    campaign = Campaign(name="OneTake AI Launch", start_date=datetime.date(2024, 12, 1), stages=stages)

    # Print initial summary
    print("Initial Campaign Summary:")
    print(campaign.get_summary())

    # Advance through campaign stages
    campaign.advance_stage()  # Move to "Pre-Launch"
    campaign.advance_stage()  # Move to "Launch"

    # Update performance metrics
    campaign.update_metrics(emails_sent=500, open_rate=45.5, click_rate=25.2)

    # Visualize campaign performance
    campaign.visualize_performance()

    # Final campaign summary
    print("Final Campaign Summary:")
    print(campaign.get_summary())
