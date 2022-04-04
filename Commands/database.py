from start import BotConfig

class DataBase:
    def dbChecks(id):
        for Database in open(f"Commands/{BotConfig().dbFile}", "r").readlines():
            Database = Database.strip("\n")
            try:
                if (int(Database.split()[0])) != (int(id)):   pass
                elif (int(Database.split()[0])) == (int(id)): return True
                else:   pass
            except: return f"Error with reading Temporary DB [{BotConfig().dbFile}]"
        return False

    def PlanCheck(id):
        for CheckPlan in open(f"Commands/Plans/{id}", "r").readlines():
            try:
                Plan = (str(CheckPlan.strip("\n").split()[0]))
                return Plan
            except:
                return False
    
    def ExpiryCheck(id):
        for CheckExpiry in open(f"Commands/Expiry/{id}", "r").readlines():
            Expiry = CheckExpiry.strip("\n").split()[0]
            if "/" not in Expiry:   return False
            elif "/" in Expiry: return Expiry