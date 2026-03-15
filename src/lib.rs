use pyo3::prelude::*;

/// A computationally heavy function simulating financial data processing.
/// It takes a large list of floats, performs complex math, and returns statistics.
#[pyfunction]
fn process_financial_data(data: Vec<f64>) -> PyResult<(f64, f64, f64)> {
    let mut sum = 0.0;
    let mut min_val = f64::MAX;
    let mut max_val = f64::MIN;

    // Iterate through millions of rows incredibly fast
    for &value in data.iter() {
        // Simulate a complex transformation (e.g., volatility adjustment calculation)
        // In pure Python, running math operations like .sin(), .powf() in a loop is very slow.
        let adjusted = (value.powf(1.5) / 2.0).sin().abs() * value;
        
        sum += adjusted;
        
        if adjusted < min_val {
            min_val = adjusted;
        }
        if adjusted > max_val {
            max_val = adjusted;
        }
    }

    let mean = sum / data.len() as f64;
    
    // Return a tuple of (mean, min, max) back to Python
    Ok((mean, min_val, max_val))
}

/// This defines the Python module. The name must match the [lib] name in Cargo.toml.
#[pymodule]
fn fast_stats(_py: Python, m: &PyModule) -> PyResult<()> {
    // Expose our Rust function to Python
    m.add_function(wrap_pyfunction!(process_financial_data, m)?)?;
    Ok(())
}