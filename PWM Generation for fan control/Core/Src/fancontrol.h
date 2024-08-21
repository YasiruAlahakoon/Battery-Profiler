// Author: Warren Jayakumar
// Define a type definition for PID
typedef struct {
	float kp;
	float ki;
	float kd;
	float prev_error;
	float integral;
	float dt;
} PID_HandleTypeDef;

// Function prototypes
void PID_Init(PID_HandleTypeDef *pid, float kp, float ki, float kd, float dt);
float PID_Compute(PID_HandleTypeDef *pid, float setpoint, float measured);
float Convert_ADCValue_To_Temperature(uint32_t adcValue);
ADC_HandleTypeDef hadc1;
TIM_HandleTypeDef htim2;

// Initialize PID
void PID_Init(PID_HandleTypeDef *pid, float kp, float ki, float kd, float dt) {
	pid->kp = kp;
	pid->ki = ki;
	pid->kd = kd;
	pid->prev_error = 0;
	pid->integral = 0;
	pid->dt = dt;
}

// Function to calculate PID output
float PID_Compute(PID_HandleTypeDef *pid, float setpoint, float measured) {
	float error = setpoint - measured;
	pid->integral += error * pid->dt;
	float derivative = (error - pid->prev_error) / pid->dt;
	pid->prev_error = error;

	float output = (pid->kp * error) + (pid->ki * pid->integral)
			+ (pid->kd * derivative);
	return output;
}

// Temeprature conversion for ADC
float Convert_ADCValue_To_Temperature(uint32_t adcValue) {
	// Convert the ADC value to temperature (example for LM35 sensor)
	float voltage = (adcValue / 4095.0) * 3.3;
	float temperature = voltage * 100.0;
	return temperature;
}
