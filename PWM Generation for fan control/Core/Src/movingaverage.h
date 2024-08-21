// Written by Yasiru Alahakoon

uint8_t size = 10; // Here, we use 10 point moving average

typedef struct {
    float array[10];
    uint8_t index;
} MovingAverageArray;

void InitMovingAverageArray(MovingAverageArray *maArray)
{
    for (uint8_t i = 0; i < size; i++) {
        maArray->array[i] = 0.0f;
    }
    maArray->index = 0;
}

void UpdateMovingAverageArray(MovingAverageArray *maArray, float newValue)
{
    maArray->array[maArray->index] = newValue;
    maArray->index = (maArray->index + 1) % size;
}

float ComputeMovingAverage(MovingAverageArray *maArray)
{
    float sum = 0;
    for (uint8_t i = 0; i < size; i++) {
        sum += maArray->array[i];
    }
    return sum / size;
}
// Below functions will need to be implemented. For now, we just return average readings
float GetVoltage(void)
{
    return (float)(rand() % 100);
}

float GetCurrent(void)
{
    return (float)(rand() % 100);
}

float GetPower(void)
{
    return (float)(rand() % 100);
}

float GetEnergy(void)
{
    return (float)(rand() % 100);
}
