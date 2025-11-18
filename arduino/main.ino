#include "secrets.h"
#include <SPI.h>
#include <MFRC522.h>

void setup() {
  Serial.begin(9600);
  setupLcd();
  setupRfid();
  setupAWS();
  
  connectToWiFi();
}

void loop() {
  loopWiFi();
  loopAWS();

  loopRfid();
  loopLcd();
}

/*void checkForMessages() {
  if (isWaitingForMessage && millis() > messageCooldown) {
    username = "";
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Error...");
    delay(1500);
    lcd.clear();
    delay(250);
    isAllowed = false;
    isWaitingForMessage = false;
    anyMessageReceived = false;
    messageCooldown = 0;
    return;
  }
  if (!isWaitingForMessage) {
    return;
  }
  if (!anyMessageReceived) {
    return;
  }

  String messageToDisplay = isAllowed ? "Bienvenido!" : "Acceso Denegado.";
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(messageToDisplay);
  
  lcd.setCursor(0,1);
  lcd.print(username);

  delay(1500);
  lcd.clear();
  delay(250);
  
  isAllowed = false;
  isWaitingForMessage = false;
  anyMessageReceived = false;
  messageCooldown = 0;
  username = "";
}

void checkForRfid() {
  if (isWaitingForMessage) {
    return;
  }

  if (!rfid.PICC_IsNewCardPresent()) {
    rfid.PCD_Init();
    return;
  }

  if (!rfid.PICC_ReadCardSerial()) {
    return;
  }

  // Try to read UID.
  String uid = "";
  for (byte i = 0; i < rfid.uid.size; i++) {
    if (rfid.uid.uidByte[i] < 0x10) {
      uid += "0";
    }
    uid += String(rfid.uid.uidByte[i], HEX);
  }
  uid.toUpperCase();
  if (lastUidChecked == uid) {
    return;
  }
  lastUidChecked = uid;

  Serial.println("Readed RFID card with UID: " + uid);

  isWaitingForMessage = sendUidCode(uid.c_str());
  if (!isWaitingForMessage) {
    Serial.println("An error has occurred while sending the Uid.");
  }
  else {
    Serial.println("Sended message, waiting for response.");
    lcd.print("Comprobando...");
    messageCooldown = millis() + WAITING_FOR_MESSAGE_COOLDOWN;
  }
}*/