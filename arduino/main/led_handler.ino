#define LED_PIN 15
#define LED_BLINK_TIME 100
#define LED_BLINK_MAX 5

enum LedState {
  LED_IDLE,
  LED_SUCCESS,
  LED_ERROR_BLINK
};

static LedState ledState = LED_IDLE;
static unsigned long ledStateUntil = 0;
static int ledErrorBlinkCount = 0;
static bool ledErrorBlinkOn = false;

void setupLed() {
  pinMode(LED_PIN, OUTPUT);
  logInfo("LED", String("Initialized on pin ") + String(LED_PIN));
}

void ledSuccess(int ledTime) {
  ledState = LED_SUCCESS;
  ledStateUntil = millis() + ledTime;
  digitalWrite(LED_PIN, HIGH);
}

void ledError(int ledTime) {
  ledState = LED_ERROR_BLINK;
  ledErrorBlinkCount = 0;
  ledErrorBlinkOn = true;
  ledStateUntil = millis() + ledTime;
  digitalWrite(LED_PIN, HIGH);
}

void loopLed() {
  unsigned long now = millis();
    if (ledState == LED_IDLE) {
        return;
    }

    if (now < ledStateUntil) {
        return;
    }

    if (ledState == LED_SUCCESS) {
        ledState = LED_IDLE;
        digitalWrite(LED_PIN, LOW);
    } else if (ledState == LED_ERROR_BLINK) {
        if (ledErrorBlinkOn) {
            digitalWrite(LED_PIN, LOW);
            ledErrorBlinkOn = false;
        } else {
            digitalWrite(LED_PIN, HIGH);
            ledErrorBlinkOn = true;
            ledErrorBlinkCount++;
        }

        if (ledErrorBlinkCount >= LED_BLINK_MAX) {
            ledState = LED_IDLE;
            digitalWrite(LED_PIN, LOW);
        } else {
            ledStateUntil = now + LED_BLINK_TIME;
        }
    }
}