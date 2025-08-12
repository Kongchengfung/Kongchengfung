
import sys
import itertools
from collections import deque

# -------------------------------
# PARSER: Reads the file and parses the KB and Query
# -------------------------------
def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    mode = None
    kb = []
    query = ''
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line == "TELL":
            mode = "TELL"
            continue
        elif line == "ASK":
            mode = "ASK"
            continue
        if mode == "TELL":
            kb.append(line)
        elif mode == "ASK":
            query = line
    return kb, query

# -------------------------------
# EXTRACT SYMBOLS
# -------------------------------
def extract_symbols(kb):
    symbols = set()
    for clause in kb:
        if "=>" in clause:
            premises, conclusion = map(str.strip, clause.split("=>"))
            premise_list = [p.strip() for p in premises.split("&")]
            symbols.update(premise_list)
            symbols.add(conclusion)
        else:
            symbols.add(clause.strip())
    return list(symbols)


# -------------------------------
# TRUTH TABLE ALGORITHM - RETURNS COUNT OF MODELS
# -------------------------------
def tt_check_all_count(kb, query, symbols, model):
    if not symbols:
        if pl_true(kb, model):
            return 1 if pl_true([query], model) else 0
        return 0
    else:
        P = symbols[0]
        rest = symbols[1:]
        model_true = model.copy()
        model_false = model.copy()
        model_true[P] = True
        model_false[P] = False
        return (tt_check_all_count(kb, query, rest, model_true) +
                tt_check_all_count(kb, query, rest, model_false))

# -------------------------------
# ENTRY POINT FOR TT ENTAILMENT + COUNT
# -------------------------------
def truth_table_entails(kb, query):
    symbols = extract_symbols(kb + [query])
    count = tt_check_all_count(kb, query, symbols, {})
    return count

def tt_check_all_count_and_total(kb, query, symbols, model):
    if not symbols:
        if pl_true(kb, model):
            if pl_true([query], model):
                return 1, 1
            else:
                return 0, 1
        return 0, 0
    else:
        P = symbols[0]
        rest = symbols[1:]
        model_true = model.copy()
        model_false = model.copy()
        model_true[P] = True
        model_false[P] = False

        yes1, total1 = tt_check_all_count_and_total(kb, query, rest, model_true)
        yes2, total2 = tt_check_all_count_and_total(kb, query, rest, model_false)
        return yes1 + yes2, total1 + total2


# -------------------------------
# FORWARD CHAINING
# -------------------------------
def forward_chaining_entails(kb, query):
    facts = set()
    rules = []
    count = {}
    inferred = {}
    agenda = deque()

    for clause in kb:
        if "=>" not in clause:
            symbol = clause.strip()
            facts.add(symbol)
            agenda.append(symbol)
        else:
            premises, conclusion = map(str.strip, clause.split("=>"))
            premise_list = [p.strip() for p in premises.split("&")]
            rule_key = (tuple(premise_list), conclusion)
            rules.append(rule_key)
            count[rule_key] = len(premise_list)

    entailed = []

    while agenda:
        p = agenda.popleft()
        if p not in inferred:
            inferred[p] = True
            entailed.append(p)
            for premise_list, conclusion in rules:
                if p in premise_list:
                    rule_key = (tuple(premise_list), conclusion)
                    count[rule_key] -= 1
                    if count[rule_key] == 0:
                        if conclusion not in inferred:
                            agenda.append(conclusion)

    return (query in entailed), entailed


# -------------------------------
# BACKWARD CHAINING
# -------------------------------
def backward_chaining_entails(kb, query):
    facts = set()
    rules = []
    inferred = set()
    visited = set()
    trace = []

    # Parse the KB into facts and Horn clauses
    for clause in kb:
        if "=>" in clause:
            premises, conclusion = map(str.strip, clause.split("=>"))
            premise_list = [p.strip() for p in premises.split("&")]
            rules.append((premise_list, conclusion.strip()))
        else:
            facts.add(clause.strip())

    def bc_ask(q):
        if q in facts:
            if q not in trace:
                trace.append(q)
            return True
        if q in visited:
            return False  # prevent falsely returning True
        visited.add(q)
        for premise_list, conclusion in rules:
            if conclusion == q:
                all_proven = True
                for p in premise_list:
                    if not bc_ask(p):
                        all_proven = False
                        break
                if all_proven:
                    if q not in trace:
                        trace.append(q)
                    return True
        return False


    result = bc_ask(query)
    return result, trace


# -------------------------------
# Evaluate KB under a model
# -------------------------------
def pl_true(clauses, model):
    for clause in clauses:
        if "=>" in clause:
            premises, conclusion = map(str.strip, clause.split("=>"))
            premise_list = [p.strip() for p in premises.split("&")]
            # If all premises are true, then conclusion must be true
            if all(model.get(p, False) for p in premise_list):
                if not model.get(conclusion, False):
                    return False
        else:
            # Atomic fact must be true
            if not model.get(clause.strip(), False):
                return False
    return True

# -------------------------------
# MAIN PROGRAM ENTRY
# -------------------------------
def main():
    if len(sys.argv) != 3:
        print("Usage: iengine <filename> <method>")
        return
    filename = sys.argv[1]
    method = sys.argv[2].upper()
    kb, query = parse_file(filename)
    print("KB:", kb)
    print("Query:", query)
    
    if method == "TT":
        symbols = extract_symbols(kb + [query])
        yes, total = tt_check_all_count_and_total(kb, query, symbols, {})
        if total > 0 and yes == total:
            print(f"YES: {yes}")
        else:
            print("NO")

    elif method == "FC":
        result, entailed = forward_chaining_entails(kb, query)
        if result:
            print("YES: " + ", ".join(sorted(entailed)))
        else:
            print("NO")

    elif method == "BC":
        result, trace = backward_chaining_entails(kb, query)
        if result:
            print("YES: " + ", ".join(trace))
        else:
            print("NO")

    else:
        print("Only TT implemented yet. FC and BC coming next.")

if __name__ == "__main__":
    main()
