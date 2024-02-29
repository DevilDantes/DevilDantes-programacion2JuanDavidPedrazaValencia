package com.mycompany.vehiculo;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Vehiculo {
    public static void main(String[] args) {
        // Crear un objeto de la clase VehiculoClase
        VehiculoClase vehiculo = new VehiculoClase();
        
        // Establecer los valores de las propiedades del vehículo
        vehiculo.setMarca("Acme Tires");
        vehiculo.setTipodellantas("Todo terreno");
        vehiculo.setModelo("TrailBlazer XT");
        vehiculo.setNumerodematricula("ABC-123");
        vehiculo.setTipodeenergia("Hidrógeno");
        vehiculo.setPaisdeorigen("Nueva Zelanda");
        
        // Crear una nueva ventana
        JFrame ventana = new JFrame("Información del vehículo");
        ventana.setSize(400, 300);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Crear un panel para agregar componentes
        JPanel panel = new JPanel();
        ventana.add(panel);
        placeComponents(panel, vehiculo);
        
        ventana.setVisible(true);
    }
    
    private static void placeComponents(JPanel panel, VehiculoClase vehiculo) {
        panel.setLayout(null);
        
        JLabel marcaLabel = new JLabel("Marca: " + vehiculo.getMarca());
        marcaLabel.setBounds(10, 20, 300, 25);
        panel.add(marcaLabel);
        
        JLabel tipoLlantaLabel = new JLabel("Tipo de llanta: " + vehiculo.getTipodellantas());
        tipoLlantaLabel.setBounds(10, 50, 300, 25);
        panel.add(tipoLlantaLabel);
        
        JLabel modeloLabel = new JLabel("Modelo: " + vehiculo.getModelo());
        modeloLabel.setBounds(10, 80, 300, 25);
        panel.add(modeloLabel);
        
        JLabel matriculaLabel = new JLabel("Número de matrícula: " + vehiculo.getNumerodematricula());
        matriculaLabel.setBounds(10, 110, 300, 25);
        panel.add(matriculaLabel);
        
        JLabel energiaLabel = new JLabel("Tipo de energía: " + vehiculo.getTipodeenergia());
        energiaLabel.setBounds(10, 140, 300, 25);
        panel.add(energiaLabel);
        
        JLabel paisLabel = new JLabel("País de origen: " + vehiculo.getPaisdeorigen());
        paisLabel.setBounds(10, 170, 300, 25);
        panel.add(paisLabel);
    }
}
