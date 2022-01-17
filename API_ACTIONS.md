# Play Roulette!
## Api List
- ##### The App Handles 3 major uses cases:
    1. **/api/user/**  for User management
    2. **/api/roulette/** for Game management
    2. **/api/roulette/bet** for Bet management
- ##### Basic Authentication has been implemented using permissions:
    1. **UL** - Checks if user is logged-in or Read Only
    2. **AL** - Checks is user is an admin i.e., Dealer(s)/Superuser

`API SYNTAX:` Method :: Endpoint - Action Name | Permission

### Documentation
---
- GET :: / - Swagger UI documentation
- GET :: /api/ - Redoc documentation
- GET :: /api/raw - raw yaml documentation

### User Management
---
- POST :: /api/user/register - Register User | UL
- DELETE :: /api/user/delete - Delete User | UL
- PUT :: /api/user/update - Update User | UL
- GET :: /api/user/view/`<str:id>` - View User By Email(id) | UL
- POST :: /api/user/deposit - Deposit Funds | UL
- POST :: /api/user/withdraw - Withdraw Funds | UL
- POST :: /api/user/transfer/`<str:id1>`/`<str:id2>` - Transfer Funds | UL

### Game Management
---
- POST :: /api/roulette/create - Create Game | AL
- DELETE :: /api/roulette/remove - Remove Game | AL
- PUT :: /api/roulette/update - Update Game | AL
- GET :: /api/roulette/activate/`<str:id>` - Activate Game | AL
- GET :: /api/roulette/deactivate/`<str:id>` - Deactivate Game | AL
- GET :: /api/roulette/view/ - View All Games | UL
- GET :: /api/roulette/view/`<str:id>` - View Game by gameID | UL

### **Bet Management**
---
- POST :: /api/roulette/bet/create - Place Bet | UL
- GET :: /api/roulette/bet/activate/`<str:id>` - Activate Bet | AL
- GET :: /api/roulette/bet/deactivate/`<str:id>` - Deactivate Bet | AL
- GET :: /api/roulette/bet/ - View All Bets | AL
- GET :: /api/roulette/bet/dealer/`<str:id>` - View All Bets by dealerID | AL
- GET :: /api/roulette/bet/player/`<str:id>` - View All Bets by playerID | AL
- GET :: /api/roulette/bet/game/`<str:id>` - View All Bets by gameID | AL
- GET :: /api/roulette/bet/resolve - Resolve all active bets | AL
- GET :: /api/roulette/bet/resolve/`<str:id>` - Resolve active bets by GameID| AL