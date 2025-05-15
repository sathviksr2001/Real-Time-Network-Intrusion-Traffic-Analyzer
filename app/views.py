from flask import Blueprint, render_template, jsonify
from .packet_sniffer import packets_data, anomalies

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('dashboard.html')

@main.route('/data')
def data():
    return jsonify({
        'total_packets': len(packets_data),
        'anomalies': len(anomalies)
    })
