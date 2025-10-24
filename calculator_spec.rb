require_relative 'calculator'

RSpec.describe Calculator do
  let(:calc) { Calculator.new }

  describe '#add' do
    it 'adds two positive numbers' do
      expect(calc.add(2, 3)).to eq(5)
    end

    it 'adds negative numbers' do
      expect(calc.add(-5, -3)).to eq(-8)
    end

    it 'adds positive and negative' do
      expect(calc.add(10, -5)).to eq(5)
    end
  end

  describe '#subtract' do
    it 'subtracts two numbers' do
      expect(calc.subtract(10, 5)).to eq(5)
    end

    it 'handles negative results' do
      expect(calc.subtract(3, 8)).to eq(-5)
    end
  end

  describe '#multiply' do
    it 'multiplies two numbers' do
      expect(calc.multiply(4, 5)).to eq(20)
    end

    it 'multiplies by zero' do
      expect(calc.multiply(5, 0)).to eq(0)
    end

    it 'multiplies negative numbers' do
      expect(calc.multiply(-3, -4)).to eq(12)
    end
  end

  describe '#divide' do
    it 'divides two numbers' do
      expect(calc.divide(10, 2)).to eq(5)
    end

    it 'raises error on division by zero' do
      expect { calc.divide(10, 0) }.to raise_error(ArgumentError, 'Division by zero')
    end

    it 'handles decimal results' do
      expect(calc.divide(10, 4)).to eq(2)
    end
  end
end
