# Password Strength Checker

Questa applicazione è stata sviluppata da **Nicola Capancioni** ed è progettata per aiutare gli utenti a verificare la forza delle loro password. Utilizzando un'interfaccia grafica intuitiva basata su Tkinter, il programma fornisce un'analisi dettagliata della complessità delle password inserite.

## Funzionalità

- **Verifica password comuni**: Il programma controlla se la password è presente nella famosa lista `rockyou.txt`, nota per contenere milioni di password comunemente utilizzate.
- **Valutazione della forza della password**: Analizza la lunghezza della password e la presenza di lettere maiuscole, minuscole, numeri e caratteri speciali.
- **Feedback visivo e testuale**: Fornisce un punteggio da 0 a 7 e una valutazione qualitativa (Weak, Okay, Good, Strong) con un'interfaccia chiara e colori distintivi.

## Installazione

1. **Clona il repository**:
   ```bash
   git clone https://github.com/tuo-username/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Requisiti**:
   Assicurati di avere Python installato sul tuo sistema. Se necessario, installa il pacchetto Tkinter:
   ```bash
   pip install tk
   ```

3. **Aggiungi il file delle password comuni**:
   Scarica `rockyou.txt` e posizionalo nella directory corretta:
   ```
   C:\\Users\\nicol\\desktop\\pypsw\\rockyou.txt
   ```
   Se desideri utilizzare un percorso diverso, modifica il percorso nel codice.

## Utilizzo

1. **Avvia l'applicazione**:
   ```bash
   python pswweakness.py
   ```

2. **Inserisci la password** nel campo dedicato e clicca su "Verifica".

3. **Leggi il risultato**:
   - Se la password è comune, verrà visualizzato un avviso.
   - Verrà fornita una valutazione della forza con un punteggio su 7.

## Come funziona

- **Verifica Password Comuni**: Il programma legge il file `rockyou.txt` e confronta la password inserita con quelle nella lista.
- **Calcolo della Forza**: Il programma valuta la password in base a:
  - Lunghezza della password.
  - Presenza di lettere maiuscole e minuscole.
  - Presenza di numeri e caratteri speciali.
  - Ogni criterio soddisfatto aumenta il punteggio.
- **Output Visivo**: I risultati sono mostrati in un box centrato con colori diversi per facilitare la comprensione:
  - **Arancione** per avvisi.
  - **Rosso** per password deboli.
  - **Verde** per password forti.


## Licenza

Questo progetto è rilasciato sotto la licenza MIT. Consulta il file [LICENSE](LICENSE) per ulteriori dettagli.

---

Sviluppato da **Nicola Capancioni** 💻

