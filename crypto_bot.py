import random
from datetime import datetime

class CryptoAdvisorBot:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "symbol": "BTC"
            },
            "Ethereum": {
                "price_trend": "stable", 
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "symbol": "ETH"
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "symbol": "ADA"
            },
            "Solana": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "symbol": "SOL"
            },
            "Polkadot": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "symbol": "DOT"
            }
        }
        
        self.greetings = [
            "Hey there! Ready to find some green and growing cryptos? 🌱",
            "Hello! Let's explore sustainable crypto investments together! 💚",
            "Hi! I'm CryptoBuddy - your AI financial sidekick! 🚀"
        ]
        
        self.help_responses = [
            "I can help you find profitable and sustainable cryptocurrencies!",
            "Ask me about trending coins, sustainable options, or specific crypto info!",
            "Need investment advice? I've got you covered! Try asking about profitability or sustainability."
        ]

    def get_greeting(self):
        return random.choice(self.greetings)

    def analyze_profitability(self):
        """Find coins with best profitability potential"""
        profitable_coins = []
        for coin, data in self.crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]:
                score = 0
                score += 10 if data["price_trend"] == "rising" else 0
                score += 10 if data["market_cap"] == "high" else 5
                profitable_coins.append((coin, score, data))
        
        profitable_coins.sort(key=lambda x: x[1], reverse=True)
        return profitable_coins[:3]

    def analyze_sustainability(self):
        """Find coins with best sustainability scores"""
        sustainable_coins = []
        for coin, data in self.crypto_db.items():
            if data["sustainability_score"] >= 7 and data["energy_use"] == "low":
                sustainable_coins.append((coin, data["sustainability_score"], data))
        
        sustainable_coins.sort(key=lambda x: x[1], reverse=True)
        return sustainable_coins[:3]

    def analyze_balanced(self):
        """Find coins that balance profitability and sustainability"""
        balanced_coins = []
        for coin, data in self.crypto_db.items():
            profit_score = 0
            profit_score += 10 if data["price_trend"] == "rising" else 5
            profit_score += 10 if data["market_cap"] == "high" else 5
            
            sustain_score = data["sustainability_score"]
            
            # Combined score (60% profitability, 40% sustainability)
            total_score = (profit_score * 0.6) + (sustain_score * 0.4)
            balanced_coins.append((coin, total_score, data))
        
        balanced_coins.sort(key=lambda x: x[1], reverse=True)
        return balanced_coins[:3]

    def get_coin_info(self, coin_name):
        """Get detailed information about a specific coin"""
        for coin, data in self.crypto_db.items():
            if coin_name.lower() in coin.lower() or coin_name.lower() in data["symbol"].lower():
                return coin, data
        return None, None

    def format_coin_response(self, coin, data, reason):
        """Format a beautiful response for coin recommendations"""
        trends = {
            "rising": "📈 Rising",
            "stable": "➡️ Stable", 
            "falling": "📉 Falling"
        }
        
        energy_emojis = {
            "high": "🔴",
            "medium": "🟡", 
            "low": "🟢"
        }
        
        response = f"\n**{coin} ({data['symbol']})**\n"
        response += f"• Price Trend: {trends[data['price_trend']]}\n"
        response += f"• Market Cap: {data['market_cap'].title()}\n"
        response += f"• Energy Use: {energy_emojis[data['energy_use']]} {data['energy_use'].title()}\n"
        response += f"• Sustainability: {'🌱' * (data['sustainability_score'] // 2)} {data['sustainability_score']}/10\n"
        response += f"💡 **Why I recommend it:** {reason}\n"
        
        return response

    def generate_response(self, user_input):
        """Main method to generate bot responses"""
        user_input = user_input.lower()
        
        # Greeting
        if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
            return self.get_greeting()
        
        # Help
        if any(word in user_input for word in ["help", "what can you do", "options"]):
            return random.choice(self.help_responses)
        
        # Profitability focus
        if any(word in user_input for word in ["profit", "trending", "growing", "make money", "investment"]):
            profitable = self.analyze_profitability()
            if profitable:
                response = "🚀 **Top Profitable Coins for Growth:**\n"
                for coin, score, data in profitable:
                    reason = "Strong growth trend with solid market presence"
                    response += self.format_coin_response(coin, data, reason)
                return response + "\n💎 *Remember: Past performance ≠ future results!*"
        
        # Sustainability focus
        if any(word in user_input for word in ["sustainable", "green", "eco", "environment", "energy"]):
            sustainable = self.analyze_sustainability()
            if sustainable:
                response = "🌱 **Top Sustainable Coins:**\n"
                for coin, score, data in sustainable:
                    reason = "Excellent environmental credentials with low energy consumption"
                    response += self.format_coin_response(coin, data, reason)
                return response + "\n💚 *Green investing helps the planet!*"
        
        # Balanced approach
        if any(word in user_input for word in ["both", "balanced", "long-term", "overall", "recommend"]):
            balanced = self.analyze_balanced()
            if balanced:
                response = "⚖️ **Best Balanced Coins (Profit + Planet):**\n"
                for coin, score, data in balanced:
                    reason = "Great balance of growth potential and sustainability"
                    response += self.format_coin_response(coin, data, reason)
                return response + "\n🌟 *Diversification is key to smart investing!*"
        
        # Specific coin info
        for coin in self.crypto_db.keys():
            if coin.lower() in user_input or self.crypto_db[coin]["symbol"].lower() in user_input:
                coin_name, data = self.get_coin_info(coin)
                if coin_name:
                    response = f"🔍 **{coin_name} Analysis:**\n"
                    response += self.format_coin_response(coin_name, data, "Detailed analysis provided above")
                    advice = self._get_coin_advice(coin_name, data)
                    return response + f"\n💡 **My Take:** {advice}"
        
        # Default response
        return "🤔 I'm not sure I understand. Try asking about:\n• 'Profitable coins'\n• 'Sustainable cryptos' \n• 'Best balanced investments'\n• Or ask about specific coins like Bitcoin or Cardano!\n\n💡 Type 'help' for more options!"

    def _get_coin_advice(self, coin, data):
        """Generate specific advice for a coin"""
        advice = []
        
        if data["price_trend"] == "rising":
            advice.append("currently in an upward trend")
        elif data["price_trend"] == "stable":
            advice.append("showing stability")
        else:
            advice.append("caution advised on trends")
            
        if data["sustainability_score"] >= 7:
            advice.append("excellent sustainability credentials")
        elif data["sustainability_score"] >= 5:
            advice.append("moderate sustainability")
        else:
            advice.append("consider environmental impact")
            
        if data["market_cap"] == "high":
            advice.append("well-established with lower volatility risk")
        else:
            advice.append("higher growth potential but more volatility")
            
        return "This coin is " + ", ".join(advice) + "."

    def get_disclaimer(self):
        """Important risk disclaimer"""
        return "\n⚠️ **IMPORTANT DISCLAIMER:** Cryptocurrency investing carries substantial risk. This is educational content only, not financial advice. Always do your own research (DYOR) and consider consulting a financial advisor. Never invest more than you can afford to lose! 🔐"

def main():
    bot = CryptoAdvisorBot()
    
    print("=" * 60)
    print(f"🤖 Welcome to {bot.name} - Your AI Financial Sidekick!")
    print("=" * 60)
    print(bot.get_greeting())
    print("\n" + bot.get_disclaimer())
    print("\n" + "=" * 60)
    
    while True:
        print("\n💬 How can I help you with your crypto journey?")
        print("   (Type 'quit' to exit, 'help' for options)")
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"\n{bot.name}: Thanks for chatting! Remember: Invest wisely! 🚀")
            break
            
        if user_input == "":
            continue
            
        response = bot.generate_response(user_input)
        print(f"\n{bot.name}: {response}")

if __name__ == "__main__":
    main()